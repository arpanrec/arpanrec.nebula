"""
This module provides functionality to fetch and manage Terraform version details.

Classes:
    Terraform(AppDetails): A class to fetch and manage Terraform version details.

Methods:
    fetch_details(self) -> None:
        Fetches the version details for Terraform. If a specific version is not provided, it fetches the latest version
        details from the Terraform releases URL. Constructs the download link for the Terraform binary based on the 
        fetched or provided version and the system architecture.

Attributes:
    __terraform_releases_url (str): URL to fetch Terraform releases information.
    __terraform_ansible_architecture_map (Dict[str, str]): Mapping of system architectures to Terraform architectures.

"""

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

        display.vvv("AppDetails Terraform: Fetching Terraform version")

        _terraform_release_tag = self._kwargs.get("terraform_rv_version", None)
        if not _terraform_release_tag or _terraform_release_tag == self._FETCH_LATEST_KEY:
            display.vvv(
                f"AppDetails Terraform: Fetching terraform version details from {self.__terraform_releases_url}."
            )
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
