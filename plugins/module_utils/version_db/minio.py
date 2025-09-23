#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module provides the minio class, which extends the AppDetails class to fetch
minio releases.

Classes:
    Minio: A class to fetch and manage minio application details.

Minio class:
    Attributes:
        __github_repo (str): The GitHub repository for minio.
        __minio_architecture_map (dict): A mapping of architecture names to minio architecture names.

    Methods:
        fetch_details(): Fetches the minio version details from GitHub or uses the provided version tag.

"""

from ansible.utils.display import Display  # type: ignore

from .grs import github_release_tag_search

# pylint: disable=E0401,E0611
from .models import AppDetails  # type: ignore

display = Display()


class Minio(AppDetails):
    """
    Minio app details.
    """

    __github_repo: str = "minio/minio"

    __minio_architecture_map: dict[str, str] = {
        "amd64": "amd64",
        "x86_64": "amd64",
        "aarch64": "arm64",
    }

    def fetch_details(self) -> None:
        _github_release_tag = self._kwargs.get("minio_rv_version", None)
        if not _github_release_tag or _github_release_tag == self._FETCH_LATEST_KEY:
            display.vvv("AppDetails minio: Fetching minio version details from GitHub.")
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
            display.vvv(f"AppDetails minio: Using provided minio version tag: {_github_release_tag}")
        # pylint: disable=attribute-defined-outside-init
        self._download_link = (
            "https://dl.min.io/server/minio/release/linux-"
            f"{self._get_ansible_architecture(self.__minio_architecture_map)}/archive/minio.{_github_release_tag}"
        )

        self._version = _github_release_tag
