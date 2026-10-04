"""Fixtures compartilhadas dos testes do cvm-fetcher."""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import pytest


@dataclass
class _HttpLog:
    """Registro dos downloads simulados."""

    downloaded: list[tuple[str, Path]] = field(default_factory=list)


class _FakeHttpClient:
    """Dublê de ``HttpClient`` que grava bytes e registra chamadas."""

    def __init__(self) -> None:
        self.log = _HttpLog()
        self.payload = b"col1;col2\n1;2\n3;4\n"

    def download_with_manifest(
        self,
        url: str,
        target_path: str | Path,
        **kwargs: Any,
    ) -> Path:
        """Simular download atômico com manifesto sidecar."""
        target = Path(target_path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(self.payload)
        manifest = target.with_name(f"{target.name}.manifest.json")
        manifest.write_text("{}", encoding="utf-8")
        self.log.downloaded.append((url, target))
        return target

    def head_last_modified_date(self, url: str) -> Any:
        """Simular freshness check (sem rede)."""
        return None


@pytest.fixture
def fake_http_client() -> _FakeHttpClient:
    """Fornecer dublê de HttpClient para injeção no CvmClient."""
    return _FakeHttpClient()


@pytest.fixture
def data_dir(tmp_path: Path) -> Iterator[Path]:
    """Diretório temporário de dados (raiz do repositório)."""
    yield tmp_path / "cvm"
