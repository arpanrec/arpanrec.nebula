from typing import Dict
from ansible.utils.display import Display  # type: ignore

from .grs import github_release_tag_search  # type: ignore

# pylint: disable=E0401,E0611
from .models import AppDetails  # type: ignore

display = Display()


class BitwardenDesktop(AppDetails):  # pylint: disable=too-few-public-methods
    """
    Bitwarden Desktop app details.
    """

    __github_repo: str = "bitwarden/clients"
    __github_release_prefix: str = "desktop-v"
    _github_release_tag: str | None

    __bitwarden_desktop_architecture_map: Dict[str, str] = {"x86_64": "x86_64"}

    def fetch_details(self) -> None:
        """
        Get the version details for the Bitwarden Desktop app.
        """

        display.vvv("AppDetails BitwardenDesktop: Fetching Bitwarden Desktop version details.")

        _github_release_tag = self._kwargs.get("bitwarden_desktop_rv_version", None)
        if not _github_release_tag or _github_release_tag == self._FETCH_LATEST_KEY:
            display.vvv("AppDetails BitwardenDesktop: Fetching Bitwarden Desktop version details from GitHub.")
            _github_release_tag = github_release_tag_search(
                github_release_tag_search_repo=self.__github_repo,
                github_release_tag_search_api_url=self._kwargs.get("github_release_tag_search_api_url"),
                github_release_tag_search_token=self._kwargs.get("github_release_tag_search_token"),
                github_release_tag_search_prefix=self.__github_release_prefix,
                github_release_tag_search_contains=self._kwargs.get("github_release_tag_search_contains"),
                github_release_tag_search_max_pages=int(self._kwargs.get("github_release_tag_search_max_pages", 100)),
                github_release_tag_search_timeout=self._kwargs.get("github_release_tag_search_timeout", 10),
            )
            display.vvv(f"AppDetails BitwardenDesktop: Latest Bitwarden Desktop version tag: {_github_release_tag}")
        else:
            display.vvv(
                f"AppDetails BitwardenDesktop: Using provided Bitwarden Desktop version tag: {_github_release_tag}"
            )

        # pylint: disable=attribute-defined-outside-init
        self._download_link = (
            f"https://github.com/bitwarden/clients/releases/download/{_github_release_tag}"
            f"/Bitwarden-{_github_release_tag[len(self.__github_release_prefix):]}"
            f"-{self._get_ansible_architecture(self.__bitwarden_desktop_architecture_map)}.AppImage"
        )
        display.vvv(f"AppDetails BitwardenDesktop: Download link: {self._download_link}")
        self._version = _github_release_tag
        display.vvv(f"AppDetails BitwardenDesktop: Version: {self._version}")
