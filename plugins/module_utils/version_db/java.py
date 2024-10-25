# pylint: disable=E0401,E0611
from typing import Any, Dict

from ansible.utils.display import Display  # type: ignore
from packaging.version import parse as parse_version

from .models import AppDetails  # type: ignore

display = Display()


class Java(AppDetails):
    """
    Class to handle Java version details.
    """

    __java_download_map: Dict[str, Any] = {
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
        "maven": {
            "maven-3.9.9": {},
            "maven-3.8.4": {},
        },
        "gradle": {
            "v8.10.2": {},
            "v7.6.4": {},
        },
        "groovy": {"4.0.22": {}, "3.0.22": {}},
        "kotlinc": {
            "v2.0.21": {},
            "v2.0.20": {},
            "v1.9.25": {},
            "v1.8.0": {},
        },
    }

    __maven_github_repo = "apache/maven"

    def fetch_details(self) -> None:
        """
        Fetch the Java version details.
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
        self._extras = {
            "maven": self._fetch_maven_version(),
            "gradle": self._fetch_gradle_version(),
            "groovy": self._fetch_groovy_version(),
            "kotlinc": self._fetch_kotlinc_version(),
        }

    def _fetch_maven_version(self) -> Dict[str, str]:
        """
        Fetch the latest Maven version.
        """
        display.vvv("AppDetails Java: Fetching Maven version details.")
        _github_release_tag = self._kwargs.get("java_rv_jdk_mvn_version", None)

        if not _github_release_tag or _github_release_tag == self._FETCH_LATEST_KEY:
            display.vvv("Fetching Maven version details.")
            # pylint: disable=R0801
            _github_release_tag = list(self.__java_download_map["maven"].keys())[0]
        else:
            if _github_release_tag not in self.__java_download_map["maven"]:
                raise ValueError(
                    f"AppDetails Java: Provided Maven version {_github_release_tag} is not supported."
                    f" Supported versions are {list(self.__java_download_map['maven'].keys())}"
                )
            display.vvv(f"Using provided Maven version tag: {_github_release_tag}")

        if not _github_release_tag or not _github_release_tag.startswith("maven-"):
            raise ValueError(
                "AppDetails Java: Failed to fetch Maven version details."
                f" Invalid Maven version tag: {_github_release_tag}",
                "Maven version tag should start with 'maven-'.",
            )
        maven_major_version = parse_version(f"{_github_release_tag[6:]}").major
        return {
            "version": _github_release_tag,
            "download_link": f"https://dlcdn.apache.org/maven/maven-{maven_major_version}"
            f"/{_github_release_tag[6:]}/binaries"
            f"/apache-{_github_release_tag}-bin.tar.gz",
        }

    def _fetch_gradle_version(self) -> Dict[str, str]:
        """
        Fetch the latest Gradle version.
        """
        display.vvv("AppDetails Java: Fetching Gradle version details.")
        _github_release_tag = self._kwargs.get("java_rv_jdk_gradle_version", None)

        if not _github_release_tag or _github_release_tag == self._FETCH_LATEST_KEY:
            display.vvv("Fetching Gradle version details.")
            # pylint: disable=R0801
            _github_release_tag = list(self.__java_download_map["gradle"].keys())[0]
        else:
            if _github_release_tag not in self.__java_download_map["gradle"]:
                raise ValueError(
                    f"AppDetails Java: Provided Gradle version {_github_release_tag} is not supported."
                    f" Supported versions are {list(self.__java_download_map['gradle'].keys())}"
                )
            display.vvv(f"Using provided Gradle version tag: {_github_release_tag}")

        return {
            "version": _github_release_tag,
            "download_link": f"https://downloads.gradle.org/distributions/gradle-{_github_release_tag[1:]}-all.zip",
        }

    def _fetch_groovy_version(self) -> Dict[str, str]:
        """
        Fetch the latest Groovy version.
        """
        display.vvv("AppDetails Java: Fetching Groovy version details.")
        _github_release_tag = self._kwargs.get("java_rv_jdk_groovy_version", None)

        if not _github_release_tag or _github_release_tag == self._FETCH_LATEST_KEY:
            display.vvv("Fetching Groovy version details.")
            # pylint: disable=R0801
            _github_release_tag = list(self.__java_download_map["groovy"].keys())[0]
        else:
            if _github_release_tag not in self.__java_download_map["groovy"]:
                raise ValueError(
                    f"AppDetails Java: Provided Groovy version {_github_release_tag} is not supported."
                    f" Supported versions are {list(self.__java_download_map['groovy'].keys())}"
                )
            display.vvv(f"Using provided Groovy version tag: {_github_release_tag}")

        return {
            "version": _github_release_tag,
            "download_link": f"https://groovy.jfrog.io/artifactory/dist-release-local/groovy-zips"
            f"/apache-groovy-sdk-{_github_release_tag}.zip",
        }

    def _fetch_kotlinc_version(self) -> Dict[str, str]:
        """
        Fetch the latest Kotlin compiler version.
        """
        display.vvv("AppDetails Java: Fetching Kotlin compiler version details.")
        _github_release_tag = self._kwargs.get("java_rv_jdk_kotlinc_version", None)

        if not _github_release_tag or _github_release_tag == self._FETCH_LATEST_KEY:
            display.vvv("Fetching Kotlin compiler version details.")
            # pylint: disable=R0801
            _github_release_tag = list(self.__java_download_map["kotlinc"].keys())[0]
        else:
            if _github_release_tag not in self.__java_download_map["kotlinc"]:
                raise ValueError(
                    f"AppDetails Java: Provided Kotlin compiler version {_github_release_tag} is not supported."
                    f" Supported versions are {list(self.__java_download_map['kotlinc'].keys())}"
                )
            display.vvv(f"Using provided Kotlin compiler version tag: {_github_release_tag}")

        return {
            "version": _github_release_tag,
            "download_link": f"https://github.com/JetBrains/kotlin/releases/download"
            f"/{_github_release_tag}/kotlin-compiler-{_github_release_tag[1:]}.zip",
        }
