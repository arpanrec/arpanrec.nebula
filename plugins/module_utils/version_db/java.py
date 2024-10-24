# pylint: disable=E0401,E0611
from typing import Dict

from .grs import github_release_tag_search
from .models import AppDetails  # type: ignore
from ansible.utils.display import Display  # type: ignore
from packaging.version import parse as parse_version

display = Display()


class Java(AppDetails):
    """
    Class to handle Java version details.
    """

    __java_download_map = {
        "jdk": {
            "21": {
                "x86_64": "https://download.oracle.com/java/21/archive/jdk-21.0.4_linux-x64_bin.tar.gz",
                "aarch64": "https://download.oracle.com/java/21/archive/jdk-21.0.4_linux-aarch64_bin.tar.gz",
            },
            "17": {
                "x86_64": "https://download.oracle.com/java/17/archive/jdk-17.0.12_linux-x64_bin.tar.gz",
                "aarch64": "https://download.oracle.com/java/17/archive/jdk-17.0.12_linux-aarch64_bin.tar.gz",
            },
        },
        "graalvm": {
            "21": {
                "x86_64": "https://download.oracle.com/graalvm/21/latest/graalvm-jdk-21_linux-x64_bin.tar.gz",
                "aarch64": "https://download.oracle.com/graalvm/21/latest/graalvm-jdk-21_linux-aarch64_bin.tar.gz",
            },
            "17": {
                "x86_64": "https://download.oracle.com/graalvm/17/latest/graalvm-jdk-17_linux-x64_bin.tar.gz",
                "aarch64": "https://download.oracle.com/graalvm/17/latest/graalvm-jdk-17_linux-aarch64_bin.tar.gz",
            },
        },
    }

    __maven_github_repo = "apache/maven"

    def fetch_details(self) -> None:
        """
        Fetch the Java version details.S
        """

        display.vvv("AppDetails Java: Fetching Java version details.")

        _java_version = self._kwargs.get("java_rv_jdk_version", None)
        _ansible_architecture = self._get_ansible_architecture()
        if not _java_version or _java_version == self._FETCH_LATEST_KEY:
            _java_version = list(self.__java_download_map["jdk"].keys())[0]
            display.vvv(f"AppDetails Java: Using Java version: {_java_version}")
        else:
            display.vvv(f"AppDetails Java: Using provided Java version: {_java_version}")
            if _java_version not in self.__java_download_map["jdk"]:
                raise ValueError(
                    f"AppDetails Java: Provided Java version {_java_version} is not supported."
                    f" Supported versions are {list(self.__java_download_map['jdk'].keys())}"
                )

        self._download_link = self.__java_download_map["jdk"][_java_version][_ansible_architecture]
        self._version = _java_version
        self._extras = {"maven": self._fetch_maven_version()}

    def _fetch_maven_version(self) -> Dict[str, str]:
        """
        Fetch the latest Maven version.
        """
        display.vvv("AppDetails Java: Fetching Maven version details.")
        _github_release_tag = self._kwargs.get("java_rv_jdk_mvn_version", None)

        if not _github_release_tag or _github_release_tag == self._FETCH_LATEST_KEY:
            display.vvv("Fetching Maven version details from GitHub.")
            # pylint: disable=R0801
            _github_release_tag = github_release_tag_search(
                github_release_tag_search_repo=self.__maven_github_repo,
                github_release_tag_search_api_url=self._kwargs.get("github_release_tag_search_api_url"),
                github_release_tag_search_token=self._kwargs.get("github_release_tag_search_token"),
                github_release_tag_search_contains=self._kwargs.get("github_release_tag_search_contains"),
                github_release_tag_search_max_pages=int(self._kwargs.get("github_release_tag_search_max_pages", 100)),
                github_release_tag_search_timeout=self._kwargs.get("github_release_tag_search_timeout", 10),
            )
        else:
            display.vvv(f"Using provided Maven version tag: {_github_release_tag}")

        if not _github_release_tag or not _github_release_tag.startswith("maven-"):
            raise ValueError(
                "AppDetails Java: Failed to fetch Maven version details."
                f" Invalid Maven version tag: {_github_release_tag}",
                "Maven version tag should start with 'maven-'.",
            )
        maven_major_version = parse_version("_github_release_tag[6:]").major
        return {
            "version": _github_release_tag,
            "download_link": f"https://dlcdn.apache.org/maven/maven-{maven_major_version}"
                             f"/{_github_release_tag[6:]}/binaries"
                             f"/apache-{_github_release_tag}-bin.tar.gz",
        }
