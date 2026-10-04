"""Armazenamento local de datasets cvm-fetcher.

Layout canônico: ``{root}/{grupo}/{arquivo}`` com carimbos temporais
``{slug}@{YYYYMMDD}.{ext}`` e ``{slug}_{particao}@{YYYYMMDD}.{ext}``:
``cad_cia_aberta@20261003.csv``, ``dfp_cia_aberta_2026@20261003.zip`` e
``inf_diario_fi_2026-10@20261003.zip``.
"""

from __future__ import annotations

import datetime as dt
from pathlib import Path
from typing import Any

from quantilica.core.storage import (
    BaseDataRepository,
    build_stamped_filename,
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
    ) -> Path:
        """Calcular o caminho local de uma entrada de dataset.

        Convenções por particionamento:

        - estático: ``{grupo}/{slug}@{stamp}.{ext}``
        - anual: ``{grupo}/{slug}_{ano}@{stamp}.{ext}``
        - mensal: ``{grupo}/{slug}_{ano}-{mes:02d}@{stamp}.{ext}``

        Args:
            entry: Entrada no schema canônico do SDK (``group``, ``id``,
                ``ext`` e ``year``/``month`` opcionais).
            last_modified: Data de modificação remota para o carimbo.

        Returns:
            Path: Caminho local do arquivo.
        """
        dataset_id = str(entry.get("group") or entry.get("id") or "datasets")
        ext = str(entry.get("ext") or "csv")
        year = entry.get("year")
        month = entry.get("month")
        slug = str(entry.get("id") or dataset_id)

        if year is not None and month is not None:
            filename = build_stamped_filename(
                slug,
                f"{int(year)}-{int(month):02d}",
                ext=ext,
                timestamp=last_modified,
            )
        elif year is not None:
            filename = build_stamped_filename(
                slug, int(year), ext=ext, timestamp=last_modified
            )
        else:
            filename = stamp_filename(slug, ext, last_modified)

        return self.dataset_path(dataset_id, filename)

    def target_for_entry(
        self,
        entry: dict[str, Any],
        *,
        last_modified: dt.date | None = None,
    ) -> Path:
        """Alias semântico de :meth:`path_for_entry` para o cliente HTTP.

        Args:
            entry: Entrada no schema canônico do SDK.
            last_modified: Data de modificação remota para o carimbo.

        Returns:
            Path: Caminho local do arquivo.
        """
        return self.path_for_entry(entry, last_modified=last_modified)
