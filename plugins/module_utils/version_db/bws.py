from ansible.utils.display import Display  # type: ignore

# pylint: disable=E0401,E0611
from ansible_collections.arpanrec.nebula.plugins.module_utils.version_db import AppDetails  # type: ignore

# pylint: disable=E0401,E0611
from ansible_collections.arpanrec.nebula.plugins.module_utils.version_db.grs import (  # type: ignore
    github_release_tag_search,
)

display = Display()


class BWS(AppDetails):  # pylint: disable=too-few-public-methods
    """
    BWS app details.
    """

    __github_repo: str = "bitwarden/sdk"
    __github_release_prefix: str = "bws-"
    _github_release_tag: str | None

    def fetch_details(self) -> None:
        """
        Get the version details for the BWS app.
        """

        _github_release_tag = self._kwargs.get("bws_sdk_version_tag", None)
        if not _github_release_tag or _github_release_tag == "fetch_latest_version":
            display.vvv("Fetching BWS version details from GitHub.")
            _github_release_tag = github_release_tag_search(
                github_release_tag_search_repo=self.__github_repo,
                github_release_tag_search_api_url=self._kwargs.get("github_release_tag_search_api_url"),
                github_release_tag_search_token=self._kwargs.get("github_release_tag_search_token"),
                github_release_tag_search_prefix=self.__github_release_prefix,
                github_release_tag_search_contains=self._kwargs.get("github_release_tag_search_contains"),
                github_release_tag_search_max_pages=int(self._kwargs.get("github_release_tag_search_max_pages", 100)),
                github_release_tag_search_timeout=self._kwargs.get("github_release_tag_search_timeout", 10),
            )
        else:
            display.vvv(f"Using provided BWS version tag: {_github_release_tag}")

        # pylint: disable=attribute-defined-outside-init
        self._download_link = (
            f"https://github.com/bitwarden/sdk/releases/download/{_github_release_tag}"
            f"/bws-{self._get_ansible_architecture()}-unknown-linux-gnu-{_github_release_tag[5:]}.zip"
        )
        self._version = _github_release_tag
