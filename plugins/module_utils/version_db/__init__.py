import abc
import dataclasses
import enum
from typing import Any, Optional, Dict

from ansible.utils.display import Display  # type: ignore

display = Display()


class SupportedApps(enum.StrEnum):
    """
    Supported apps.
    """

    BWS = "bws"


@dataclasses.dataclass
class VersionDetails:
    """
    Version details.
    """

    download_link: str
    version: str


class AppDetails(abc.ABC):
    """
    App details.
    """

    _variables: Optional[Dict[str, Any]]
    _download_link: str
    _version: str
    _args: tuple[Any, ...]
    _kwargs: dict[str, Any]

    def __init__(self, variables: Optional[Dict[str, Any]], *args, **kwargs) -> None:  # type: ignore
        """
        Constructor.
        """
        self._variables = variables
        self._args = args
        self._kwargs = kwargs

    @abc.abstractmethod
    def fetch_details(self) -> None:
        """
        Get the version details for the app.
        """

    def get_version_details(self) -> VersionDetails:
        """
        Get the version details for the app.
        """

        return VersionDetails(download_link=self._download_link, version=self._version)


def get_version(app_name: str, variables: Optional[Dict[str, Any]], *args, **kwargs) -> VersionDetails:  # type: ignore
    """
    Get the version details for the specified app.
    """

    app = SupportedApps(app_name)
    app_details: AppDetails

    match app:
        case SupportedApps.BWS:
            from .bws import BWS  # pylint: disable=import-outside-toplevel

            app_details = BWS(variables, *args, **kwargs)
        case _:
            raise ValueError(f"Unsupported app: {app_name}")

    app_details.fetch_details()
    version_details: VersionDetails = app_details.get_version_details()

    return version_details
