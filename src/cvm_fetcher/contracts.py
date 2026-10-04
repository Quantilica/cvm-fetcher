"""Contratos tipados do catálogo e dos datasets do cvm-fetcher."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Literal

# Tipos de particionamento temporal suportados pela CVM.
CvmPartitionType = Literal["static", "annual", "monthly"]


@dataclass(frozen=True)
class DatasetEntry:
    """Uma entrada de dataset do espelho da CVM.

    Args:
        group: Identificador canônico do grupo (ex.: ``"cia-dfp"``).
        id: Slug base do arquivo (ex.: ``"dfp_cia_aberta"``).
        url: URL determinística do arquivo no espelho Nginx.
        ext: Extensão do arquivo remoto (``csv`` ou ``zip``).
        description: Descrição opcional do conjunto de dados.
        year: Ano da partição, ou None para arquivos estáticos.
        month: Mês da partição (1-12), ou None.
    """

    group: str
    id: str
    url: str
    ext: str
    description: str = ""
    year: int | None = None
    month: int | None = None

    @property
    def partition(self) -> CvmPartitionType:
        """Tipo de particionamento temporal da entrada."""
        if self.year is not None and self.month is not None:
            return "monthly"
        if self.year is not None:
            return "annual"
        return "static"

    def to_dict(self) -> dict[str, Any]:
        """Serializar a entrada no schema canônico do SDK (``FetcherApp``)."""
        data = asdict(self)
        return {k: v for k, v in data.items() if v not in ("", None)}

    @classmethod
    def validate(cls, data: dict[str, Any]) -> DatasetEntry:
        """Reconstruir uma entrada a partir de um dicionário validado.

        Args:
            data: Dicionário no schema canônico do SDK.

        Returns:
            DatasetEntry: A entrada reconstruída.

        Raises:
            ValueError: Se campos obrigatórios estiverem ausentes.
        """
        missing = {"group", "id", "url", "ext"} - set(data)
        if missing:
            msg = f"Campos obrigatórios ausentes: {sorted(missing)}"
            raise ValueError(msg)
        return cls(
            group=data["group"],
            id=data["id"],
            url=data["url"],
            ext=data["ext"],
            description=data.get("description", ""),
            year=data.get("year"),
            month=data.get("month"),
        )


@dataclass(frozen=True)
class GroupInfo:
    """Metadados de um grupo canônico de datasets.

    Args:
        id: Identificador canônico do grupo (ex.: ``"fi-inf-diario"``).
        name: Nome legível do grupo.
        description: Descrição do escopo do grupo.
        macro: Macro-domínio de origem (ex.: ``"fundos"``).
        partition: Particionamento temporal dominante do grupo.
    """

    id: str
    name: str
    description: str = ""
    macro: str = ""
    partition: CvmPartitionType | None = None

    def to_dict(self) -> dict[str, Any]:
        """Serializar o grupo no schema canônico do SDK (``FetcherApp``)."""
        return {
            "name": self.name,
            "description": self.description,
            "macro": self.macro,
            "partition": self.partition,
        }
