from ansible_collections.arpanrec.nebula.plugins.module_utils.version_db import AppDetails
from ansible_collections.arpanrec.nebula.plugins.module_utils.version_db.grs import github_release_search


class BWS(AppDetails):
    """
    BWS app details.
    """

    __github_repo: str = "bitwarden/sdk"
    __github_release_prefix: str = "bws-"

    def fetch_details(self) -> None:
        """
        Get the version details for the BWS app.
        """

        _github_release_version: str = github_release_search(
            github_repo=self.__github_repo,
            prefix=self.__github_release_prefix,
            github_token=self._kwargs.get("github_token"),
            github_api_url=self._kwargs.get("github_api_url"),
        )
        self._version = _github_release_version[5:]
        self._download_link = (
            f"https://github.com/bitwarden/sdk/releases/download/bws-v{self._version}/bws-"
            f"test-unknown-linux-gnu-{self._version}.zip"
        )
