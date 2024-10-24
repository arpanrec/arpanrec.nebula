import abc
import dataclasses
import enum
import json
from typing import Any, Dict, Optional, Tuple

from ansible.utils.display import Display  # type: ignore

display = Display()


class SupportedApps(enum.Enum):
    """
    Supported apps.
    """

    BWS = "bws"
    TERRAFORM = "terraform"
    CODE = "code"
    VAULT = "vault"
    BITWARDEN_DESKTOP = "bitwarden_desktop"


@dataclasses.dataclass
class VersionDetails:
    """
    Version details.
    """

    download_link: str
    version: str
    checksum: Optional[str] = None
    extras: Optional[Dict[str, Any]] = None


class AppDetails(abc.ABC):
    """
    App details.
    """

    __metaclass__ = abc.ABCMeta

    _variables: Optional[Dict[str, Any]]
    _download_link: str
    _version: str
    _args: Tuple[Any, ...]
    _extras: Optional[Dict[str, Any]]
    _kwargs: Dict[str, Any]
    _checksum: Optional[str] = None
    _FETCH_LATEST_KEY = "fetch_latest_version"

    def __init__(self, *args, **kwargs) -> None:  # type: ignore
        """
        Constructor.
        """

        self._variables = kwargs.get("variables")
        self._args = args
        self._kwargs = kwargs

    @abc.abstractmethod
    def fetch_details(self) -> None:
        """
        Get the version details for the app.
        """

    def _get_ansible_architecture(self, ansible_to_expected: Optional[Dict[str, str]] = None) -> str:
        """
        Get the architecture from the Ansible facts.
        """

        if not self._variables:
            raise ValueError("Hostvars not provided.")

        if not self._variables.get("ansible_architecture", None):
            raise ValueError("ansible_architecture not found in hostvars. Make sure gather_facts is enabled.")

        ansible_architecture: str = self._variables["ansible_architecture"]

        if not ansible_to_expected:
            display.vvv(f"Ansible architecture selected as: {ansible_architecture}")
            return ansible_architecture

        if ansible_architecture not in ansible_to_expected:
            raise ValueError(
                f"Unsupported architecture: {ansible_architecture}, Supported Only in:"
                f" {json.dumps(ansible_to_expected)}"
            )
        return ansible_to_expected[ansible_architecture]

    def get_version_details(self) -> VersionDetails:
        """
        Get the version details for the app.
        """

        return VersionDetails(
            download_link=self._download_link, version=self._version, checksum=self._checksum, extras=self._extras
        )
