#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module provides functionality to fetch and manage version details for the Visual Studio Code (VSCode) application.

Classes:
    Code: Inherits from AppDetails and provides methods to fetch VSCode version details.

Attributes:
    __code_releases_url (str): URL to fetch the stable releases of VSCode.
    __code_ansible_architecture_map (Dict[str, str]): Mapping of Ansible architecture to VSCode architecture.

Methods:
    fetch_details(self) -> None: Fetches the version details for the VSCode application.

"""

from typing import Dict, List

import requests
from ansible.utils.display import Display  # type: ignore

# pylint: disable=E0401,E0611
from .models import AppDetails  # type: ignore

display = Display()


class Code(AppDetails):  # pylint: disable=too-few-public-methods
    """
    VSCODE app details.
    """

    __code_releases_url: str = "https://update.code.visualstudio.com/api/releases/stable"

    __code_ansible_architecture_map: Dict[str, str] = {"x86_64": "x64", "aarch64": "arm64"}

    def fetch_details(self) -> None:
        """
        Get the version details for the VSCODE.
        """

        display.vvv("AppDetails Code: Fetching VSCODE version details.")

        _code_release_tag = self._kwargs.get("code_rv_version", None)
        if not _code_release_tag or _code_release_tag == self._FETCH_LATEST_KEY:
            display.vvv(f"AppDetails Code: Fetching VSCode version details from {self.__code_releases_url}.")
            try:
                _vscode_releases: List[str] = requests.get(self.__code_releases_url, timeout=10).json()
                _code_release_tag = list(_vscode_releases)[0]

                display.vvv(f"AppDetails Code: Latest VSCode release tag: {_code_release_tag}")

            except Exception as e:
                display.error(f"AppDetails Code: Failed to fetch VSCode releases: {e}")
                raise ValueError(f"AppDetails Code: Failed to fetch VSCode releases. {str(e)}") from e
        else:
            display.vvv(f"AppDetails Code: Using provided VSCode version tag: {_code_release_tag}")
        # "https://update.code.visualstudio.com/1.94.2/linux-arm64/stable"
        # pylint: disable=attribute-defined-outside-init
        self._download_link = (
            f"https://update.code.visualstudio.com/{_code_release_tag}"
            f"/linux-{self._get_ansible_architecture(self.__code_ansible_architecture_map)}/stable"
        )
        self._version = _code_release_tag
