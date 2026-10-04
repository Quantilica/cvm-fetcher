"""Cliente HTTP para o espelho de dados abertos da CVM.

Encapsula o ``HttpClient`` de `quantilica-core` com verificação de frescor
(``Last-Modified``/``ETag``), gravação atômica e manifesto sidecar SHA-256
(``DownloadManifest``).
"""

from __future__ import annotations

import datetime as dt
from pathlib import Path

from quantilica.core.http import HttpClient

from ._catalog_base import CVM_BASE_URL

__all__ = ["CvmClient"]

SOURCE_ID = "cvm"
PRODUCER = "cvm-fetcher"


class CvmClient:
    """Cliente determinístico para o portal de dados abertos da CVM."""

    def __init__(
        self,
        base_url: str = CVM_BASE_URL,
        *,
        client: HttpClient | None = None,
        timeout: float = 180.0,
        attempts: int = 5,
    ) -> None:
        """Inicializar o cliente.

        Args:
            base_url: URL base do espelho de dados.
            client: Instância opcional de ``HttpClient`` (útil em testes).
            timeout: Timeout de rede em segundos.
            attempts: Tentativas por requisição em caso de falha.
        """
        self.base_url = base_url.rstrip("/")
        self.http = client or HttpClient(
            timeout=timeout,
            verify=True,
            attempts=attempts,
            retry_base_delay=2.0,
            emulate_browser=True,
        )

    def dataset_url(self, relative_path: str) -> str:
        """Montar a URL determinística de um arquivo do espelho.

        Args:
            relative_path: Caminho relativo a ``dados/`` (ex.:
                ``"CIA_ABERTA/CAD/DADOS/cad_cia_aberta.csv"``).

        Returns:
            str: URL absoluta do arquivo.
        """
        segments = "/".join(
            seg.strip("/") for seg in str(relative_path).split("/") if seg
        )
        return f"{self.base_url}/{segments}"

    def head_last_modified(self, url: str) -> dt.date | None:
        """Consultar a data de modificação remota do arquivo.

        Args:
            url: URL do arquivo remoto.

        Returns:
            dt.date | None: Data do ``Last-Modified``, ou None se
                indisponível.
        """
        try:
            return self.http.head_last_modified_date(url)
        except Exception:  # noqa: BLE001 — frescor é best-effort.
            return None

    def download_with_manifest(
        self,
        url: str,
        target: Path,
        dataset_id: str,
        *,
        force: bool = False,
    ) -> Path:
        """Baixar um arquivo com gravação atômica e manifesto sidecar.

        Realiza checagem de frescor antes do streaming (HEAD ``Last-Modified``
        + ``Content-Length``) e grava o arquivo junto ao manifest
        ``<target>.manifest.json`` com SHA-256 e proveniência.

        Args:
            url: URL do arquivo remoto.
            target: Caminho local de destino.
            dataset_id: Dataset canônico (grupo) para proveniência.
            force: Forçar re-download mesmo quando fresco.

        Returns:
            Path: Caminho do arquivo gravado (ou já fresco).

        Raises:
            HttpStatusError: Em erros HTTP não tratados pelo cliente base.
            StorageError: Em falhas de stream ou espaço em disco.
        """
        return self.http.download_with_manifest(
            url,
            target,
            source_id=SOURCE_ID,
            dataset_id=dataset_id,
            producer=PRODUCER,
            force=force,
        )
