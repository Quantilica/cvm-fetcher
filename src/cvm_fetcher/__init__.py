"""cvm-fetcher — coletor de dados abertos da CVM (Comissão de Valores Mobiliários).

Fornece ferramentas para sincronizar dados estruturados do mercado de capitais
brasileiro publicados no Portal de Dados Abertos (dados.cvm.gov.br): cadastros,
demonstrações contábeis de companhias abertas, indústria de fundos de
investimento e ofertas públicas de distribuição.
"""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("cvm-fetcher")
except PackageNotFoundError:  # pragma: no cover - ambiente sem pacote instalado
    __version__ = "0.0.0"

__all__ = ["__version__"]
