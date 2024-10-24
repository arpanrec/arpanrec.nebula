from ansible.utils.display import Display  # type: ignore

from .models import AppDetails, SupportedApps, VersionDetails

display = Display()


def get_version(app_name: str, *args, **kwargs) -> VersionDetails:  # type: ignore
    """
    Get the version details for the specified app.
    """
    app_details: AppDetails

    match app_name:
        case SupportedApps.BWS.value:
            from .bws import BWS  # pylint: disable=import-outside-toplevel

            app_details = BWS(*args, **kwargs)  # type: ignore
        case SupportedApps.TERRAFORM.value:
            from .terraform import Terraform  # pylint: disable=import-outside-toplevel

            app_details = Terraform(*args, **kwargs)  # type: ignore
        case SupportedApps.CODE.value:
            from .code import Code  # pylint: disable=import-outside-toplevel

            app_details = Code(*args, **kwargs)  # type: ignore
        case SupportedApps.VAULT.value:
            from .vault import Vault  # pylint: disable=import-outside-toplevel

            app_details = Vault(*args, **kwargs)  # type: ignore
        case SupportedApps.BITWARDEN_DESKTOP.value:
            from .bitwarden_desktop import BitwardenDesktop  # pylint: disable=import-outside-toplevel

            app_details = BitwardenDesktop(*args, **kwargs)  # type: ignore
        case _:
            raise ValueError(f"Unsupported app: {app_name}")

    app_details.fetch_details()
    version_details: VersionDetails = app_details.get_version_details()

    return version_details
