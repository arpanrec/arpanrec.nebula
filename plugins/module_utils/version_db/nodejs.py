"""
This module provides functionality to fetch and manage NodeJS application details.

Classes:
    NodeJS(AppDetails): A class to handle NodeJS application details, including fetching version details from GitHub.

Methods:
    fetch_details(self) -> None:
        Fetches the NodeJS version details from GitHub or uses a provided version tag.
          Constructs the download link for the specified NodeJS version and architecture.

Attributes:
    __github_repo (str): The GitHub repository for NodeJS releases.
    __node_architecture_map (dict[str, str]): A mapping of architecture names to NodeJS architecture identifiers.
"""

from ansible.utils.display import Display  # type: ignore

from .grs import github_release_tag_search  # type: ignore

# pylint: disable=E0401,E0611
from .models import AppDetails  # type: ignore

display = Display()


class NodeJS(AppDetails):
    """
    NodeJS app details.
    """

    __github_repo: str = "nodejs/node"

    __node_architecture_map: dict[str, str] = {
        "amd64": "x64",
        "x86_64": "x64",
        "armv7l": "armv7l",
        "aarch64": "arm64",
    }

    def fetch_details(self) -> None:
        _github_release_tag = self._kwargs.get("nodejs_rv_version", None)
        if not _github_release_tag or _github_release_tag == self._FETCH_LATEST_KEY:
            display.vvv("AppDetails NodeJS: Fetching NodeJS version details from GitHub.")
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
            display.vvv(f"AppDetails NodeJS: Using provided NodeJS version tag: {_github_release_tag}")

        # pylint: disable=attribute-defined-outside-init
        self._download_link = (
            f"https://nodejs.org/download/release"
            f"/{_github_release_tag}/node-{_github_release_tag}-linux"
            f"-{self._get_ansible_architecture(self.__node_architecture_map)}.tar.gz"
        )
        self._version = _github_release_tag
