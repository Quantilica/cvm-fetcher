"""Testes da conversão CSV/ZIP -> Parquet com proveniência ``quantilica.*``."""

from __future__ import annotations

import zipfile
from pathlib import Path

import pytest

pytest.importorskip("polars")
pytest.importorskip("quantilica.analytics.writer")

import polars as pl  # noqa: E402
import pyarrow.parquet as pq  # noqa: E402
from quantilica.core.manifests import (  # noqa: E402
    DownloadManifest,
    write_manifest_sidecar,
)

from cvm_fetcher.plugin import _convert_impl  # noqa: E402


def _write_manifest(raw: Path) -> None:
    manifest = DownloadManifest.from_content(
        source_id="cvm",
        dataset_id="teste",
        url="https://dados.cvm.gov.br/teste",
        content=raw.read_bytes(),
        producer="cvm-fetcher",
    )
    write_manifest_sidecar(raw, manifest)


def _meta(parquet: Path) -> dict[str, str]:
    raw = pq.ParquetFile(parquet).metadata.metadata or {}
    return {k.decode(): v.decode() for k, v in raw.items()}


def test_convert_csv_herda_proveniencia(tmp_path: Path) -> None:
    src, dst = tmp_path / "raw", tmp_path / "out"
    src.mkdir()
    csv = src / "a.csv"
    csv.write_bytes(b"col1;col2\n1;2\n3;4\n")
    _write_manifest(csv)

    assert _convert_impl(src, dst) == 1

    out = dst / "a.parquet"
    assert pl.read_parquet(out).shape == (2, 2)
    meta = _meta(out)
    assert meta["quantilica.source_id"] == "cvm"
    assert meta["quantilica.dataset_id"] == "teste"
    assert meta["quantilica.producer"] == "cvm-fetcher"


def test_convert_zip_herda_proveniencia_do_zip(tmp_path: Path) -> None:
    src, dst = tmp_path / "raw", tmp_path / "out"
    src.mkdir()
    zpath = src / "b.zip"
    with zipfile.ZipFile(zpath, "w") as zf:
        zf.writestr("inner.csv", "x;y\n1;2\n")
    _write_manifest(zpath)

    assert _convert_impl(src, dst) == 1

    meta = _meta(dst / "b__inner.parquet")
    assert meta["quantilica.dataset_id"] == "teste"
    assert "quantilica.origin_sha256" in meta


def test_convert_sem_manifest_nao_injeta_metadados(tmp_path: Path) -> None:
    src, dst = tmp_path / "raw", tmp_path / "out"
    src.mkdir()
    (src / "c.csv").write_bytes(b"a;b\n1;2\n")

    assert _convert_impl(src, dst) == 1

    assert not any(k.startswith("quantilica.") for k in _meta(dst / "c.parquet"))
