"""Testes do cliente HTTP (CvmClient) do cvm-fetcher."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest
from quantilica.core.http import HttpStatusError

from cvm_fetcher.catalog import list_datasets
from cvm_fetcher.client import PRODUCER, SOURCE_ID, CvmClient
from cvm_fetcher.storage import DataRepository


class _HeadClient:
    """Dublê com HEAD determinístico e download gravado."""

    def __init__(self) -> None:
        self.calls: list[tuple[str, str]] = []  # (método, url)
        self.forced = False
        self.payload = b"a;b\n1;2\n"

    def head_last_modified_date(self, url: str) -> Any:
        self.calls.append(("head", url))
        return None

    def download_with_manifest(
        self,
        url: str,
        target_path: Any,
        *,
        source_id: str,
        dataset_id: str,
        producer: str,
        force: bool = False,
        **kwargs: Any,
    ) -> Path:
        self.calls.append(("download", url))
        self.forced = force
        assert source_id == "cvm"
        assert producer == "cvm-fetcher"
        assert isinstance(dataset_id, str)
        target = Path(target_path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(self.payload)
        Path(f"{target}.manifest.json").write_text("{}", encoding="utf-8")
        return target


def test_dataset_url_builder() -> None:
    """dataset_url monta URL absoluta sobre a base configurada."""
    client = CvmClient(client=_HeadClient())
    url = client.dataset_url("CIA_ABERTA/CAD/DADOS/cad_cia_aberta.csv")
    assert url == (
        "https://dados.cvm.gov.br/dados/CIA_ABERTA/CAD/DADOS/cad_cia_aberta.csv"
    )


def test_download_with_manifest(tmp_path: Path, fake_http_client: Any) -> None:
    """Download grava arquivo + manifesto sidecar com proveniência."""
    client = CvmClient(client=fake_http_client)
    entry = next(e for e in list_datasets("cadastros") if e.id == "cad_fi")
    repo = DataRepository(tmp_path)
    target = repo.path_for_entry(entry.to_dict(), last_modified=None)

    result = client.download_with_manifest(entry.url, target, entry.group)

    assert result == target
    assert target.read_bytes() == fake_http_client.payload
    assert Path(f"{result}.manifest.json").read_text(encoding="utf-8") == "{}"
    assert SOURCE_ID == "cvm" and PRODUCER == "cvm-fetcher"


def test_provenance_metadata_forwarded(tmp_path: Path, fake_http_client: Any) -> None:
    """source_id/producer corretos são repassados ao HttpClient."""
    client = CvmClient(client=fake_http_client)
    entry = list_datasets("oferta")[0]
    target = DataRepository(tmp_path).path_for_entry(entry.to_dict())
    result = client.download_with_manifest(entry.url, target, entry.group)
    assert result == target
    assert any(url == entry.url for url, _ in fake_http_client.log.downloaded)


def test_head_last_modified_none_on_error(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Frescor é best-effort: erro no HEAD degrada para None."""

    class _BoomClient(_HeadClient):
        def head_last_modified_date(self, url: str) -> Any:
            raise RuntimeError("boom")

    client = CvmClient(client=_BoomClient())
    entry = list_datasets("oferta")[0]
    assert client.head_last_modified(entry.url) is None


def test_http_status_error_propagates(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """HttpStatusError do download base propaga ao chamador."""
    entry = list_datasets("oferta")[0]

    def _raise(self: Any, *args: Any, **kwargs: Any) -> None:
        raise HttpStatusError(url=entry.url, status_code=503)

    monkeypatch.setattr("cvm_fetcher.client.HttpClient.download_with_manifest", _raise)
    client = CvmClient()
    target = DataRepository(tmp_path).path_for_entry(entry.to_dict())
    with pytest.raises(HttpStatusError):
        client.download_with_manifest(entry.url, target, entry.group)
