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

    def target_for_entry(
        self,
        entry: dict[str, Any],
        *,
        last_modified: dt.date | None = None,
    ) -> Path:
        """Alias semântico de :meth:`path_for_entry` para o cliente HTTP."""
        return self.path_for_entry(entry, last_modified=last_modified)
