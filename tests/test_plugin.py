"""Testes do plugin Typer (FetcherApp) do cvm-fetcher."""

from __future__ import annotations

from pathlib import Path
from typing import Any, ClassVar

import pytest
from quantilica.cli.sdk import FetcherApp
from typer.testing import CliRunner

from cvm_fetcher import plugin as plugin_module
from cvm_fetcher.plugin import app, fetcher, resolve_groups

runner = CliRunner(env={"COLUMNS": "200"})


class _FakeSdkHttp:
    """Dublê de HttpClient no namespace do SDK do quantilica-cli."""

    downloads: ClassVar[list[str]] = []

    def __init__(self, **kwargs: Any) -> None:
        self.timeout = kwargs.get("timeout", 180.0)
        self.headers: dict[str, str] = kwargs.get("headers", {})
        self.follow_redirects = kwargs.get("follow_redirects", True)
        self.attempts = kwargs.get("attempts", 1)
        self.retry_base_delay = kwargs.get("retry_base_delay", 0.0)
        self.verify = kwargs.get("verify", True)
        self.limits = kwargs.get("limits", None)

    def __enter__(self) -> _FakeSdkHttp:
        return self

    def close(self) -> None:
        return None

    def head_last_modified_date(self, url: str) -> None:
        return None

    def download_with_manifest(
        self, url: str, target_path: Path, **kwargs: Any
    ) -> Path:
        self.downloads.append(url)
        target = Path(target_path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(b"a;b\n1;2\n")
        return target


@pytest.fixture
def fake_http(monkeypatch: pytest.MonkeyPatch) -> type[_FakeSdkHttp]:
    """Substituir o HttpClient do SDK pelo dublê (import + threads)."""
    _FakeSdkHttp.downloads.clear()
    monkeypatch.setattr("quantilica.cli.sdk.HttpClient", _FakeSdkHttp)
    monkeypatch.setattr(fetcher, "client", _FakeSdkHttp())
    return _FakeSdkHttp


def test_fetcher_app_canonical() -> None:
    """plugin expõe a FetcherApp canônica e usa fetcher.app como app."""
    assert isinstance(fetcher, FetcherApp)
    assert fetcher.name == "cvm-fetcher"
    assert app is fetcher.app


def test_resolve_macro_aliases() -> None:
    """make_resolve_groups aceita grupos canônicos e macro-aliases."""
    assert resolve_groups(["cia-dfp"]) == ["cia-dfp"]
    assert resolve_groups(["cadastros"]) == plugin_module.MACRO_ALIASES["cadastros"]
    assert resolve_groups(["fundos"]) == plugin_module.MACRO_ALIASES["fundos"]
    assert resolve_groups(None) == list(plugin_module.GROUPS)


def test_list() -> None:
    """list renderiza tabelas Rich de todos os grupos."""
    result = runner.invoke(app, ["list"])
    assert result.exit_code == 0
    assert "fi-inf-diario" in result.output
    assert "dataset(s) no catálogo" in result.output


def test_sync_dry_run_nao_baixa(tmp_path: Path, fake_http: Any) -> None:
    """sync --dry-run exibe plano e não baixa nada."""
    result = runner.invoke(app, ["sync", "ofertas", "-o", str(tmp_path), "--dry-run"])
    assert result.exit_code == 0
    assert _FakeSdkHttp.downloads == []
    assert "oferta_distribuicao.zip" in result.output
    assert "arquivo(s) listado(s)" in result.output


def test_sync_dry_run_multi_grupos(tmp_path: Path, fake_http: Any) -> None:
    """sync --dry-run planeja macro-alias expandido multidomínio."""
    result = runner.invoke(
        app, ["sync", "cias", "oferta", "-o", str(tmp_path), "--dry-run"]
    )
    assert result.exit_code == 0
    assert _FakeSdkHttp.downloads == []
    for g in ("cia-dfp", "cia-itr", "ofertas"):
        assert g in result.output


def test_sync_download_single_group(tmp_path: Path, fake_http: Any) -> None:
    """sync baixa de fato apenas o grupo planejado."""
    result = runner.invoke(app, ["sync", "oferta", "-o", str(tmp_path)])
    assert result.exit_code == 0
    assert any("oferta_distribuicao.zip" in u for u in _FakeSdkHttp.downloads)
    assert "Concluído:" in result.output


def test_sync_grupo_invalido_aborta(tmp_path: Path, fake_http: Any) -> None:
    """sync com grupo inválido encerra com código 1 e não baixa nada."""
    result = runner.invoke(app, ["sync", "grupo-inesistente", "-o", str(tmp_path)])
    assert result.exit_code == 1
    assert _FakeSdkHttp.downloads == []


def test_convert_registrado() -> None:
    """comando convert (comando_convert do SDK) está registrado."""
    command_names = [c.name for c in app.registered_commands]
    assert {"sync", "list", "convert"} <= set(command_names)
