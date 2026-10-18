"""Conversão de dados brutos da CVM (CSV/ZIP) para Parquet."""

from __future__ import annotations

import tempfile
from pathlib import Path

try:
    import polars as pl
    from quantilica.analytics.writer import to_parquet
    from quantilica.core.files import decompress_archive
except ImportError as exc:
    raise ImportError(
        "cvm_fetcher.wrangling requer o extra 'analysis': "
        "uv add 'cvm-fetcher[analysis]' "
        "--index https://index.quantilica.com/simple/"
    ) from exc

from .reader import read_csv_smart

__all__ = ["convert_all", "write_parquet"]


def write_parquet(
    df: pl.DataFrame, target: Path, source_path: Path | None = None
) -> Path:
    """Gravar Parquet herdando a proveniência ``quantilica.*`` do bruto.

    Args:
        df: DataFrame a gravar.
        target: Caminho do Parquet de destino.
        source_path: Arquivo bruto (``.csv``/``.zip``) cujo sidecar
            ``.manifest.json`` fornece a proveniência.

    Returns:
        Path: Caminho do Parquet gravado.
    """
    return to_parquet(df, target, source_path=source_path)


def convert_all(input_dir: Path, output_dir: Path) -> int:
    """Converter CSVs (diretos ou dentro de ZIPs) para Parquet.

    Args:
        input_dir: Diretório de origem com dados brutos.
        output_dir: Diretório de destino dos Parquet.

    Returns:
        int: Quantidade de Parquet gerados.
    """
    converted = 0
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for csv_path in sorted(input_path.rglob("*.csv")):
        rel = csv_path.relative_to(input_path)
        df = read_csv_smart(csv_path)
        write_parquet(
            df,
            output_path / rel.parent / f"{csv_path.stem}.parquet",
            source_path=csv_path,
        )
        converted += 1

    for zip_path in sorted(input_path.rglob("*.zip")):
        rel = zip_path.relative_to(input_path)
        with tempfile.TemporaryDirectory() as tmp:
            extracted = decompress_archive(zip_path, Path(tmp))
            members = (
                [extracted]
                if extracted.is_file()
                else sorted(Path(extracted).glob("*"))
            )
            for member in members:
                if member.is_file():
                    target = (
                        output_path
                        / rel.parent
                        / f"{zip_path.stem}__{member.stem}.parquet"
                    )
                    write_parquet(read_csv_smart(member), target, source_path=zip_path)
                    converted += 1
    return converted
