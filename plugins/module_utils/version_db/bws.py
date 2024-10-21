from ansible_collections.arpanrec.nebula.plugins.module_utils.version_db import AppDetails
from ansible_collections.arpanrec.nebula.plugins.module_utils.version_db.grs import github_release_search


class BWS(AppDetails):
    """
    BWS app details.
    """

    __github_repo: str = "bitwarden/sdk"

    def fetch_details(self) -> None:
        """
        Get the version details for the BWS app.
        """

        self._version: str = github_release_search(github_repo=self.__github_repo, prefix="bws-")[5:]

        self._download_link = (
            f"https://github.com/bitwarden/sdk/releases/download/bws-v{self._version}/bws-"
            f"test-unknown-linux-gnu-{self._version}.zip"
        )
