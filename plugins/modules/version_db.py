# -*- coding: utf-8 -*-
"""
Ansible Module for Search for the latest release in a GitHub repository.
"""

from __future__ import absolute_import, division, print_function

from typing import Any, Dict

from ansible.module_utils.basic import AnsibleModule  # type: ignore
from ansible_collections.arpanrec.nebula.plugins.module_utils.version_db import github_release_search

# pylint: disable=C0103,invalid-name
__metaclass__ = type

DOCUMENTATION = r"""
---
module: arpanrec.nebula.version_db
requirements:
    - python >= 3.10
description:
    - Search for the latest release in a GitHub repository.
options:
    github_repo:
        description:
            - The GitHub repository to search.
        required: true
        type: str
    github_token:
        description:
            - The GitHub token to use for authentication.
            - If not provided, the GITHUB_TOKEN environment variable will be used.
        required: false
        type: str
    github_api_url:
        description:
            - The GitHub API URL.
        required: false
        type: str
        default: "https://api.github.com"
    prefix:
        description:
            - The prefix of the tag to search for.
        required: false
        type: str
    suffix:
        description:
            - The suffix of the tag to search for.
        required: false
        type: str
    contains:
        description:
            - The substring that the tag should contain.
        required: false
        type: str
    max_pages:
        description:
            - The maximum number of pages to search.
        required: false
        type: int
        default: 100
    timeout:
        description:
            - The timeout for the request.
        required: false
        type: int
        default: 10
"""


def run_module() -> None:
    """
    Search for the latest release in a GitHub repository.
    """
    module_args: Dict[str, Dict[str, Any]] = {
        "github_repo": {"type": "str", "required": True},
        "github_token": {"type": "str", "required": False},
        "github_api_url": {"type": "str", "required": False, "default": "https://api.github.com"},
        "prefix": {"type": "str", "required": False},
        "suffix": {"type": "str", "required": False},
        "contains": {"type": "str", "required": False},
        "max_pages": {"type": "int", "required": False, "default": 100},
        "timeout": {"type": "int", "required": False, "default": 10},
    }

    result = {"changed": False, "original_message": ""}

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    tag_version = github_release_search(
        github_repo=module.params["github_repo"],
        github_token=module.params["github_token"],
        github_api_url=module.params["github_api_url"],
        prefix=module.params["prefix"],
        suffix=module.params["suffix"],
        contains=module.params["contains"],
        max_pages=module.params["max_pages"],
        timeout=module.params["timeout"],
    )

    result["tag_version"] = tag_version

    module.exit_json(**result)


def main() -> None:
    """
    Python Main Module
    """
    run_module()


if __name__ == "__main__":
    main()
