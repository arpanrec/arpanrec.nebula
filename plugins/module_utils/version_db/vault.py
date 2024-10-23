from typing import Any, Dict

import requests
from ansible.utils.display import Display  # type: ignore

from .models import AppDetails  # type: ignore

display = Display()


class Vault(AppDetails):  # pylint: disable=too-few-public-methods
    """
    Vault app details.
    """

    __vault_releases_url: str = "https://releases.hashicorp.com/vault/index.json"

    __vault_ansible_architecture_map: Dict[str, str] = {"x86_64": "amd64", "aarch64": "arm64"}

    def fetch_details(self) -> None:
        """
        Get the version details for the Vault.
        """
        _vault_release_tag = self._kwargs.get("vault_rv_version", None)
        if not _vault_release_tag or _vault_release_tag == "fetch_latest_version":
            display.vvv(f"Fetching Vault version details from {self.__vault_releases_url}.")
            try:
                _vault_releases: Dict[str, Any] = requests.get(self.__vault_releases_url, timeout=10).json()[
                    "versions"
                ]
                _vault_release_tag = list(_vault_releases)[-1]

                display.vvv(f"Latest Vault release tag: {_vault_release_tag}")

            except Exception as e:
                display.error(f"Failed to fetch Vault releases: {e}")
                raise ValueError(f"Failed to fetch Vault releases. {str(e)}") from e
        else:
            display.vvv(f"Using provided Vault version tag: {_vault_release_tag}")
        # https://releases.hashicorp.com/vault/1.4.4/vault_1.4.4_linux_amd64.zip
        # pylint: disable=attribute-defined-outside-init
        self._download_link = (
            f"https://releases.hashicorp.com/vault/{_vault_release_tag}"
            f"/vault_{_vault_release_tag}_linux_"
            f"{self._get_ansible_architecture(self.__vault_ansible_architecture_map)}.zip"
        )
        self._version = _vault_release_tag
