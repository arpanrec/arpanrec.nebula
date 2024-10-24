from typing import Any, Dict

import requests
from ansible.utils.display import Display  # type: ignore

from .models import AppDetails  # type: ignore

display = Display()


class Terraform(AppDetails):  # pylint: disable=too-few-public-methods
    """
    Terraform app details.
    """

    __terraform_releases_url: str = "https://releases.hashicorp.com/terraform/index.json"

    __terraform_ansible_architecture_map: Dict[str, str] = {"x86_64": "amd64", "aarch64": "arm64"}

    def fetch_details(self) -> None:
        """
        Get the version details for the Terraform.
        """

        display.vvv(f"AppDetails Terraform: Fetching Terraform version")

        _terraform_release_tag = self._kwargs.get("terraform_rv_version", None)
        if not _terraform_release_tag or _terraform_release_tag == self._FETCH_LATEST_KEY:
            display.vvv(f"AppDetails Terraform: Fetching terraform version details from"
                        f" {self.__terraform_releases_url}.")
            try:
                _terraform_releases: Dict[str, Any] = requests.get(self.__terraform_releases_url, timeout=10).json()[
                    "versions"
                ]
                _terraform_release_tag = list(_terraform_releases)[-1]

                display.vvv(f"AppDetails Terraform: Latest terraform release tag: {_terraform_release_tag}")

            except Exception as e:
                display.error(f"AppDetails Terraform: Failed to fetch terraform releases: {e}")
                raise ValueError(f"AppDetails Terraform: Failed to fetch terraform releases. {str(e)}") from e
        else:
            display.vvv(f"AppDetails Terraform: Using provided Terraform version tag: {_terraform_release_tag}")
        # https://releases.hashicorp.com/terraform/1.4.4/terraform_1.4.4_linux_amd64.zip
        # pylint: disable=attribute-defined-outside-init
        self._download_link = (
            f"https://releases.hashicorp.com/terraform/{_terraform_release_tag}"
            f"/terraform_{_terraform_release_tag}_linux_"
            f"{self._get_ansible_architecture(self.__terraform_ansible_architecture_map)}.zip"
        )
        self._version = _terraform_release_tag
