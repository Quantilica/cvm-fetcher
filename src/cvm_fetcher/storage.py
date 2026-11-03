"""Armazenamento local de datasets cvm-fetcher.

Layout canônico: ``{root}/{grupo}/{arquivo}`` com carimbos temporais
``{slug}@{YYYYMMDD}.{ext}`` e ``{slug}_{particao}@{YYYYMMDD}.{ext}``:
``cad_cia_aberta@20261003.csv``, ``dfp_cia_aberta_2026@20261003.zip`` e
``inf_diario_fi_2026-10@20261003.zip``.
"""

from __future__ import annotations

import datetime as dt
from pathlib import Path
from typing import Any, Literal

from quantilica.core.storage import (
    BaseDataRepository,
    build_stamped_filename,
    format_partition_token,
    stamp_filename,
)

__all__ = [
    "DEFAULT_OUTPUT",
    "DataRepository",
    "build_stamped_filename",
    "stamp_filename",
]

DEFAULT_OUTPUT = "/data/cvm"


class DataRepository(BaseDataRepository):
    """Repositório de dados da CVM (layout ``{grupo}/{arquivo}``)."""

    def __init__(self, root: Path | str = DEFAULT_OUTPUT):
        """Inicializar o repositório.

        Args:
            root: Diretório raiz de dados (padrão: ``/data/cvm``).
        """
        super().__init__(root)

    def path_for_entry(
        self,
        entry: dict[str, Any],
        *,
        last_modified: dt.date | None = None,
        precision: Literal["date", "datetime"] = "date",
        subdir_by_year: bool = False,
    ) -> Path:
        """Compute the destination path for a dataset entry with fallback timestamp.

        When ``last_modified`` is None, uses today's date as the timestamp
        to ensure all raw files are stamped (@YYYYMMDD) per A7 archetype.

        Args:
            entry: Mapping containing metadata (group, id, ext, year, etc.).
            last_modified: The last modified timestamp to stamp, or None.
            precision: The timestamp precision ("date" or "datetime").
            subdir_by_year: If True and year is present, place under
                ``{dataset_id}/{year}/``.

        Returns:
            Path: The computed local path under the storage root.
        """
        timestamp = last_modified or dt.date.today()

        dataset_id = str(
            entry.get("group") or entry.get("dataset") or entry.get("id") or "datasets"
        )
        slug = str(entry.get("id") or entry.get("slug") or dataset_id)

        ext = entry.get("ext")
        if not ext:
            tail = str(entry.get("url", "")).split("?")[0].rsplit("/", 1)[-1]
            ext = tail.rsplit(".", 1)[-1] if "." in tail else "bin"
        ext = ext.lstrip(".")

        partition = format_partition_token(entry)
        filename = build_stamped_filename(
            slug,
            partition,
            ext=ext,
            timestamp=timestamp,
            precision=precision,
        )

        year = entry.get("year") if entry.get("year") is not None else entry.get("ano")
        if subdir_by_year and year is not None and str(year).strip():
            return self.dataset_path(dataset_id, str(year).strip(), filename)
        return self.dataset_path(dataset_id, filename)

    def target_for_entry(
        self,
        entry: dict[str, Any],
        *,
        last_modified: dt.date | None = None,
    ) -> Path:
        """Alias semântico de :meth:`path_for_entry` para o cliente HTTP."""
        return self.path_for_entry(entry, last_modified=last_modified)
