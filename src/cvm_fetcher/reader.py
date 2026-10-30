"""Leitura de CSVs da CVM (requer o extra ``analysis``)."""

from __future__ import annotations

import io
import logging
import re
from pathlib import Path

try:
    import polars as pl
except ImportError as exc:
    raise ImportError(
        "cvm_fetcher.reader requer o extra 'analysis': "
        "uv add 'cvm-fetcher[analysis]' "
        "--index https://index.quantilica.com/simple/"
    ) from exc

__all__ = ["read_csv_smart"]

logger = logging.getLogger("cvm_fetcher.reader")

_RAGGED = "found more fields"
_DATE = re.compile(r"\d{4}-\d{2}-\d{2}")
# Marca provisória do ``;`` que faz parte do texto de um campo; some na leitura.
_SEMICOLON = "\x1f"


def read_csv_smart(path: Path) -> pl.DataFrame:
    """Ler CSV da CVM com separador ``;`` e fallback de encoding.

    Linhas com mais campos que o cabeçalho (um ``;`` dentro do texto de um campo,
    sem aspas) são reparadas: o ``;`` volta para o campo a que pertence, nada é
    descartado, e um aviso informa a quantidade e os números das linhas.

    Args:
        path: Arquivo CSV.

    Returns:
        pl.DataFrame: Conteúdo do CSV (tenta UTF-8, depois latin-1).
    """
    errors = []
    # Esquema inferido do arquivo inteiro: na CDA, ``CD_SELIC`` é numérico nas
    # primeiras linhas e traz texto ("PDD") mais adiante.
    # A CVM não delimita campos com aspas: elas fazem parte do texto ("Spin-off" da
    # Contax, no Assunto do IPE). Lidas como delimitador, desalinham as colunas.
    for quote in ('"', None):
        for encoding in ("utf-8", "latin-1"):
            try:
                return pl.read_csv(
                    path,
                    separator=";",
                    encoding=encoding,
                    quote_char=quote,
                    infer_schema_length=None,
                )
            except Exception as exc:  # noqa: BLE001 - próxima combinação
                errors.append(exc)
    if any(_RAGGED in str(exc) for exc in errors):
        return _read_ragged(path)
    raise errors[-1]


def _is_number(value: str) -> bool:
    try:
        float(value.strip().replace(",", "."))
    except ValueError:
        return False
    return True


def _kind(values: list[str]) -> str:
    """Classificar uma coluna como ``num``, ``date`` ou ``text`` pelos valores."""
    filled = [v for v in values if v.strip()]
    if filled and all(_is_number(v) for v in filled):
        return "num"
    if filled and all(_DATE.fullmatch(v.strip()) for v in filled):
        return "date"
    return "text"


def _fits(kind: str, value: str) -> bool:
    if not value.strip() or kind == "text":
        return True
    if kind == "num":
        return _is_number(value)
    return bool(_DATE.fullmatch(value.strip()))


def _read_ragged(path: Path) -> pl.DataFrame:
    """Ler um CSV com linhas de campos a mais, juntando o excesso ao campo de texto.

    A CVM publica alguns campos de texto livre sem aspas, e um ``;`` digitado ali
    cria um campo a mais (ex.: ``Ata da Assembleia (27052026); Sumário da`` na
    coluna ``CNPJ`` do cedente/devedor de CRA). Para cada linha assim, testa-se
    juntar os campos a mais em cada posição e fica a que melhor respeita o tipo
    das colunas vizinhas (número, data), medido nas linhas sem defeito. Empate:
    a coluna de texto mais larga nas linhas boas. O ``;`` fica no valor; só a
    leitura muda, nenhuma linha é descartada.
    """
    raw = path.read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        text = raw.decode("latin-1")
    if _SEMICOLON in text:
        raise ValueError(f"{path.name}: o arquivo já contém o caractere U+001F")
    lines = [line.rstrip("\r") for line in text.split("\n")]
    while lines and not lines[-1]:
        lines.pop()
    width = lines[0].count(";") + 1

    rows = [line.split(";") for line in lines[1:]]
    good = [r for r in rows if len(r) == width]
    kinds = [_kind([r[j] for r in good]) for j in range(width)]
    max_len = [max((len(r[j]) for r in good), default=0) for j in range(width)]

    fixed: list[str] = [lines[0]]
    repaired: list[tuple[int, str]] = []
    for number, (line, fields) in enumerate(zip(lines[1:], rows, strict=True), 2):
        if len(fields) <= width:
            fixed.append(line)
            continue
        extra = len(fields) - width
        best = min(
            range(width),
            key=lambda s: (
                sum(
                    not _fits(
                        kinds[j],
                        (_SEMICOLON.join(fields[s : s + extra + 1]))
                        if j == s
                        else fields[j if j < s else j + extra],
                    )
                    for j in range(width)
                ),
                -max_len[s],
                s,
            ),
        )
        merged = fields[:best] + [_SEMICOLON.join(fields[best : best + extra + 1])]
        merged += fields[best + extra + 1 :]
        fixed.append(";".join(merged))
        repaired.append((number, lines[0].split(";")[best]))

    columns = sorted({name for _, name in repaired})
    shown = ", ".join(str(n) for n, _ in repaired[:10])
    logger.warning(
        "%s: %d linha(s) com campos a mais; o ';' foi mantido no texto da coluna %s "
        "(linhas %s%s)",
        path.name,
        len(repaired),
        "/".join(columns),
        shown,
        ", ..." if len(repaired) > 10 else "",
    )

    data = "\n".join(fixed).encode("utf-8")
    df = None
    for quote in ('"', None):
        try:
            df = pl.read_csv(
                io.BytesIO(data),
                separator=";",
                quote_char=quote,
                infer_schema_length=None,
            )
            break
        except Exception:  # noqa: BLE001 - próxima combinação
            continue
    if df is None:
        raise ValueError(f"{path.name}: não foi possível ler o CSV após o reparo")
    text_cols = [c for c, t in df.schema.items() if t == pl.String]
    return df.with_columns(
        pl.col(c).str.replace_all(_SEMICOLON, ";", literal=True) for c in text_cols
    )
