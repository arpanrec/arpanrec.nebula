#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module provides the minio_client class, which extends the AppDetails class to fetch
minio_client releases.

Classes:
    MinioClient: A class to fetch and manage minio_client application details.

MinioClient class:
    Attributes:
        __github_repo (str): The GitHub repository for minio_client.
        __minio_client_architecture_map (dict): A mapping of architecture names to minio_client architecture names.

    Methods:
        fetch_details(): Fetches the minio_client version details from GitHub or uses the provided version tag.

"""

from ansible.utils.display import Display  # type: ignore

from .grs import github_release_tag_search

# pylint: disable=E0401,E0611
from .models import AppDetails  # type: ignore

display = Display()


class MinioClient(AppDetails):
    """
    MinioClient app details.
    """

    __github_repo: str = "minio/mc"

    __minio_client_architecture_map: dict[str, str] = {
        "amd64": "amd64",
        "x86_64": "amd64",
        "aarch64": "arm64",
    }

    def fetch_details(self) -> None:
        _github_release_tag = self._kwargs.get("minio_client_rv_version", None)
        if not _github_release_tag or _github_release_tag == self._FETCH_LATEST_KEY:
            display.vvv("AppDetails minio_client: Fetching minio_client version details from GitHub.")
            # pylint: disable=R0801
            _github_release_tag = github_release_tag_search(
                github_release_tag_search_repo=self.__github_repo,
                github_release_tag_search_api_url=self._kwargs.get("github_release_tag_search_api_url"),
                github_release_tag_search_token=self._kwargs.get("github_release_tag_search_token"),
                github_release_tag_search_contains=self._kwargs.get("github_release_tag_search_contains"),
                github_release_tag_search_max_pages=int(self._kwargs.get("github_release_tag_search_max_pages", 100)),
                github_release_tag_search_timeout=self._kwargs.get("github_release_tag_search_timeout", 10),
            )
        else:
            display.vvv(f"AppDetails minio_client: Using provided minio_client version tag: {_github_release_tag}")
        # pylint: disable=attribute-defined-outside-init
        self._download_link = (
            "https://dl.min.io/client/mc/release/linux-"
            f"{self._get_ansible_architecture(self.__minio_client_architecture_map)}/archive/mc.{_github_release_tag}"
        )

        self._version = _github_release_tag
