#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module provides functionality to retrieve version details for various supported applications.

Classes:
    Display: Utility class from ansible.utils.display for displaying messages.
    AppDetails: Base class for application details.
    SupportedApps: Enum class representing supported applications.
    VersionDetails: Class representing version details of an application.

Functions:
    get_version(app_name: str, *args, **kwargs) -> VersionDetails:

        Parameters:
            app_name (str): The name of the application.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            VersionDetails: An instance containing version details of the specified application.

        Raises:
            ValueError: If the specified app is not supported.

"""
from typing import Optional

from ansible.utils.display import Display  # type: ignore

from .models import AppDetails, SupportedApps, VersionDetails

display = Display()


def get_version(app_name: str, *args, **kwargs) -> VersionDetails:  # type: ignore
    """
    Get the version details for the specified app.
    """
    app_details: Optional[AppDetails] = None

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

        case SupportedApps.GO.value:
            from .go import Go  # pylint: disable=import-outside-toplevel

            app_details = Go(*args, **kwargs)  # type: ignore

        case SupportedApps.JAVA.value:
            from .java import Java  # pylint: disable=import-outside-toplevel

            app_details = Java(*args, **kwargs)  # type: ignore

        case SupportedApps.NODEJS.value:
            from .nodejs import NodeJS  # pylint: disable=import-outside-toplevel

            app_details = NodeJS(*args, **kwargs)  # type: ignore

        case SupportedApps.PULUMI.value:
            from .pulumi import Pulumi  # pylint: disable=import-outside-toplevel

            app_details = Pulumi(*args, **kwargs)  # type: ignore

        case SupportedApps.GITEA.value:
            from .gitea import Gitea  # pylint: disable=import-outside-toplevel

            app_details = Gitea(*args, **kwargs)  # type: ignore

        case _:
            raise ValueError(f"Unsupported app: {app_name}")

    if not app_details:
        raise ValueError(f"Unsupported app: {app_name}")

    app_details.fetch_details()
    version_details: VersionDetails = app_details.get_version_details()

    return version_details
