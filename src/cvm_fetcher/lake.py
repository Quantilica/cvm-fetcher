"""Convert raw CVM open data into the Hive-partitioned lake.

Each raw file lands in
``<lake>/cvm/<group>/[ano=<ano>/][mes=<mes>/]<file_key>.parquet``.
Monthly datasets (e.g. Informes Diários de Fundos) are partitioned by ``ano=/mes=``;
annual reports (e.g. DFP) by ``ano=``; and static registrations (cadastros) are stored
unpartitioned.
"""

from __future__ import annotations

import re
import tempfile
import zipfile
from dataclasses import dataclass, field
from pathlib import Path

try:
    import polars as pl
    from quantilica.analytics.lake import LakeError, LakeWriter
    from quantilica.core.files import decompress_archive
    from quantilica.core.lake import DatasetDescriptor, file_key, select_current
except ImportError as exc:
    raise ImportError(
        "cvm_fetcher.lake requer o extra 'analysis': "
        "uv add 'cvm-fetcher[analysis]' "
        "--index https://index.quantilica.com/simple/"
    ) from exc

from cvm_fetcher import __version__
from cvm_fetcher.catalog import GROUPS
from cvm_fetcher.reader import read_csv_smart

SOURCE_ID = "cvm"

_YM = re.compile(r"[-_](?P<ano>(?:19|20)\d{2})-(?P<mes>0[1-9]|1[0-2])(?:@|\.|$|\b)")
_Y = re.compile(r"[-_](?P<ano>(?:19|20)\d{2})(?:@|\.|$|\b)")


@dataclass
class ConvertResult:
    """Counts of a conversion run; ``errors`` holds one message per failure."""

    converted: int = 0
    skipped: int = 0
    errors: list[str] = field(default_factory=list)


def resolve_group(path: Path) -> str | None:
    """Infer group from parent folder or filename."""
    if path.parent.name in GROUPS:
        return path.parent.name
    if path.parent.parent.name in GROUPS:
        return path.parent.parent.name
    for group in GROUPS:
        if path.name.startswith(group):
            return group
    return None


def resolve_partitions(path: Path) -> tuple[list[str], dict[str, str]]:
    """Determine partition keys and values from filename or folder."""
    match_ym = _YM.search(path.name) or _YM.search(path.parent.name)
    if match_ym:
        return ["ano", "mes"], {"ano": match_ym["ano"], "mes": match_ym["mes"]}

    match_y = _Y.search(path.name) or _Y.search(path.parent.name)
    if match_y:
        return ["ano"], {"ano": match_y["ano"]}

    return [], {}


class LakeConverter:
    """Converter registered under the ``quantilica.lake`` entry point."""

    source_id = SOURCE_ID

    def datasets(self) -> list[str]:
        """Dataset ids this converter writes to the lake."""
        return sorted(GROUPS)

    def convert(
        self,
        input_dir: Path,
        lake_dir: Path,
        *,
        datasets: list[str] | None = None,
        force: bool = False,
    ) -> ConvertResult:
        """Convert raw CVM files into ``lake_dir``.

        Args:
            input_dir: Root directory containing raw CVM files.
            lake_dir: Root of the lake.
            datasets: Optional list of group names to convert.
            force: Reconvert even if sha256 already matches in the lake.

        Returns:
            ConvertResult: Files converted, skipped, and error messages.
        """
        input_dir = Path(input_dir)
        lake_dir = Path(lake_dir)
        result = ConvertResult()
        if not input_dir.is_dir():
            result.errors.append(f"diretório '{input_dir}' não existe")
            return result

        allowed = set(datasets) if datasets else set(GROUPS)
        unknown = allowed - set(GROUPS)
        if unknown:
            for u in sorted(unknown):
                result.errors.append(f"dataset desconhecido: {u}")
            return result

        candidates = sorted(
            p
            for p in input_dir.rglob("*")
            if p.is_file() and p.suffix.lower() in {".csv", ".zip"}
        )
        # The raw folder keeps every snapshot of a file (``x@20261027.zip``,
        # ``x@20261028.zip``...), and they all map to one lake file. Converting each
        # one in turn made them overwrite each other, so the next run found the
        # lake holding the wrong version and reconverted. Only the newest snapshot
        # is current; the older ones count as skipped.
        current = set(
            select_current(p.relative_to(input_dir).as_posix() for p in candidates)
        )
        files = []
        for path in candidates:
            if path.relative_to(input_dir).as_posix() in current:
                files.append(path)
                continue
            group = resolve_group(path)
            if group and group in allowed:
                result.skipped += 1

        writers: dict[str, LakeWriter] = {}

        for path in files:
            group = resolve_group(path)
            if not group or group not in allowed:
                continue

            part_keys, part_vals = resolve_partitions(path)
            writer_key = f"{group}:" + ",".join(part_keys)

            if writer_key not in writers:
                writers[writer_key] = LakeWriter(
                    lake_dir / SOURCE_ID / group,
                    DatasetDescriptor(
                        source_id=SOURCE_ID,
                        dataset_id=group,
                        alias=group,
                        partition_keys=part_keys,
                        partition_types={k: "varchar" for k in part_keys},
                    ),
                    force=force,
                )
            writer = writers[writer_key]

            if path.suffix.lower() == ".csv":
                try:
                    df = read_csv_smart(path)
                    written = writer.write_polars(
                        df,
                        path,
                        partitions=part_vals,
                        converter=f"cvm-fetcher {__version__}",
                    )
                    if written.status == "skipped":
                        result.skipped += 1
                    else:
                        result.converted += 1
                except (
                    LakeError,
                    OSError,
                    pl.exceptions.PolarsError,
                    Exception,
                ) as exc:
                    message = str(exc).strip()
                    first_line = message.splitlines()[0] if message else repr(exc)
                    result.errors.append(f"{path.name}: {first_line}")
                    continue

            elif path.suffix.lower() == ".zip":
                with tempfile.TemporaryDirectory() as tmp:
                    try:
                        extracted = decompress_archive(path, Path(tmp))
                        # ``decompress_archive`` returns just the first data file of
                        # a multi-file archive; every CSV in the ZIP goes to the lake.
                        members = sorted(
                            m
                            for m in Path(tmp).rglob("*")
                            if m.is_file() and m.suffix.lower() == ".csv"
                        )
                        if not members and extracted.is_file():
                            members = [extracted]
                        for member in members:
                            if not member.is_file():
                                continue
                            df = read_csv_smart(member)
                            key = f"{file_key(path)}__{file_key(member)}"
                            written = writer.write_polars(
                                df,
                                path,
                                partitions=part_vals,
                                file_key_name=key,
                                converter=f"cvm-fetcher {__version__}",
                            )
                            if written.status == "skipped":
                                result.skipped += 1
                            else:
                                result.converted += 1
                    except (
                        LakeError,
                        OSError,
                        zipfile.BadZipFile,
                        pl.exceptions.PolarsError,
                        Exception,
                    ) as exc:
                        message = str(exc).strip()
                        first_line = message.splitlines()[0] if message else repr(exc)
                        result.errors.append(f"{path.name}: {first_line}")
                        continue

        return result


converter = LakeConverter()
