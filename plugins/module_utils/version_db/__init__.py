import dataclasses
import enum

from ansible.utils.display import Display  # type: ignore

from .grs import github_release_search

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


def get_version(app_name: str, ansible_architecture: str) -> VersionDetails:
    """
    Get the version details for the specified app.
    """

    display.v(f"ansible_architecture: {ansible_architecture}")
    if not ansible_architecture:
        raise ValueError("ansible_architecture is expected, make sure ansible_facts is present")
    app = SupportedApps(app_name)
    display.v(f"app: {app}, {str(type(app))}")
    vd = VersionDetails(download_link="", version="")
    vd.download_link = f"dl-{ansible_architecture}"
    vd.version = "version"
    return vd
