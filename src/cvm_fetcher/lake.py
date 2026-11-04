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
from typing import Any

try:
    import polars as pl
    from quantilica.analytics.lake import LakeError, LakeWriter
    from quantilica.core.files import decompress_archive
    from quantilica.core.lake import (
        DatasetDescriptor,
        composite_file_key,
        partition_types_for,
        select_current,
    )
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

DATASET_ALIASES: dict[str, str] = {
    "securit-cri": "securitizacao_cri",
    "securit-cra": "securitizacao_cra",
    "ofertas": "ofertas_distribuicao",
    "fidc-inf-mensal": "inf_mensal_fidc",
    "fip-inf": "inf_quadrimestral_fip",
}

REVERSE_DATASET_ALIASES: dict[str, str] = {v: k for k, v in DATASET_ALIASES.items()}
REVERSE_DATASET_ALIASES.update(
    {v.replace("_", "-"): k for k, v in DATASET_ALIASES.items()}
)

_YM = re.compile(r"[-_](?P<ano>(?:19|20)\d{2})-(?P<mes>0[1-9]|1[0-2])(?:@|\.|$|\b)")
_Y = re.compile(r"[-_](?P<ano>(?:19|20)\d{2})(?:@|\.|$|\b)")


def _cast_code_columns(df: pl.DataFrame) -> pl.DataFrame:
    """Garante que CNPJ, ISIN e códigos CVM permaneçam como pl.String."""
    exprs = []
    for col in df.columns:
        norm = col.lower().replace("-", "_")
        if any(key in norm for key in ("cnpj", "isin", "codigo_cvm", "cd_cvm")):
            if df.schema[col] != pl.String:
                exprs.append(pl.col(col).cast(pl.String))
    return df.with_columns(exprs) if exprs else df


def _detect_code_overrides(path: Path) -> dict[str, Any]:
    """Detecta colunas de código pelo cabeçalho para leitura direta como pl.String."""
    try:
        with open(path, "rb") as f:
            line = f.readline().decode("latin-1", errors="replace").strip()
        headers = [h.strip('" ') for h in line.split(";")]
        overrides: dict[str, Any] = {}
        for h in headers:
            norm = h.lower().replace("-", "_")
            if any(key in norm for key in ("cnpj", "isin", "codigo_cvm", "cd_cvm")):
                overrides[h] = pl.String
        return overrides
    except Exception:
        return {}


def _read_csv_with_codes(path: Path) -> pl.DataFrame:
    """Lê um CSV da CVM mantendo CNPJ, ISIN e códigos CVM como ``pl.String``."""
    df = read_csv_smart(path, schema_overrides=_detect_code_overrides(path))
    return _cast_code_columns(df)


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

        allowed: set[str] = set()
        if datasets:
            unknown: set[str] = set()
            for d in datasets:
                target = REVERSE_DATASET_ALIASES.get(d, d)
                if target in GROUPS:
                    allowed.add(target)
                else:
                    unknown.add(d)
            if unknown:
                for u in sorted(unknown):
                    result.errors.append(f"dataset desconhecido: {u}")
                return result
        else:
            allowed = set(GROUPS)

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
                alias = DATASET_ALIASES.get(group, group.replace("-", "_"))
                writers[writer_key] = LakeWriter(
                    lake_dir / SOURCE_ID / group,
                    DatasetDescriptor(
                        source_id=SOURCE_ID,
                        dataset_id=group,
                        alias=alias,
                        partition_keys=part_keys,
                        partition_types=partition_types_for(part_keys),
                    ),
                    force=force,
                )
            writer = writers[writer_key]

            if path.suffix.lower() == ".csv":
                try:
                    df = _read_csv_with_codes(path)
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
                            df = _read_csv_with_codes(member)
                            member_name = member.stem
                            key = composite_file_key(path, member_name)
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
