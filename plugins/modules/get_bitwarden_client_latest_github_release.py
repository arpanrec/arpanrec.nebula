"""
Ansible Module for Searching the latest bitwarden client release version from github.
"""

from __future__ import absolute_import, division, print_function

from typing import Any

import requests
from ansible.module_utils.basic import AnsibleModule  # type: ignore

# pylint: disable=C0103,invalid-name
__metaclass__ = type

DOCUMENTATION = r"""
---
module: get_bitwarden_client_latest_github_release
"""


def run_module(which: str = "desktop") -> None:
    """
    Get the latest bitwarden client release version from github
    """
    module_args: dict[str, Any] = {}

    tag_version = None
    url = "https://api.github.com/repos/bitwarden/clients/releases"

    headers = {
        "Accept": "application/vnd.github.v3+json",
    }

    params = {
        "per_page": 50,
    }

    page_num = 0
    is_tag_found = False

    while True:
        params["page"] = page_num
        response = requests.get(url, headers=headers, params=params, timeout=10)
        if response.status_code != 200:
            raise ValueError(f"Error fetching releases: {response.status_code}, {response.text}")
        response_data = response.json()
        if len(response_data) == 0:
            break
        for release in response_data:
            tag_name = release["tag_name"]
            if tag_name.lower().startswith(f"{which}-"):
                is_tag_found = True
                tag_version = tag_name.replace(f"{which}-", "", 1)
                break
        if is_tag_found:
            break
        page_num += 1
        print(f"Page {page_num} processed")
    if not is_tag_found:
        raise ValueError(f"No tag found for f{which}")

    result = {"changed": False, "original_message": "", "message": ""}

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    result["msg"] = tag_version

    module.exit_json(**result)


def main() -> None:
    """
    Python Main Module
    """
    run_module()


if __name__ == "__main__":
    main()
