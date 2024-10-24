from typing import Dict, List

import requests
from ansible.utils.display import Display  # type: ignore

# pylint: disable=E0401,E0611
from .models import AppDetails  # type: ignore

display = Display()


class Go(AppDetails):  # pylint: disable=too-few-public-methods
    """
    GoLang app details.
    """

    raise NotImplementedError("GoLang app details are not implemented yet.")
