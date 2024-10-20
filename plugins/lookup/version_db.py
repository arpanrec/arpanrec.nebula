# -*- coding: utf-8 -*-
"""
Ansible Module for Search for the latest release in a GitHub repository.
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import json
from dataclasses import asdict
from typing import List, Dict, Any, Optional

from ansible.errors import AnsibleLookupError  # type: ignore
from ansible.plugins.lookup import LookupBase  # type: ignore
from ansible.utils.display import Display  # type: ignore
from ansible_collections.arpanrec.nebula.plugins.module_utils.version_db import get_version, VersionDetails

DOCUMENTATION = """
---
    name: version_db
    author:
        - Jonathan Lung (@lungj) <lungj@heresjono.com>
    short_description: Get version details.
    version_added: 5.4.0
    description:
        - Get version details.
    options:
        _terms:
            description: Key(s) to fetch values for from login info.
            required: true
            type: list
            elements: str
"""


def run_module() -> None:
    """
    Search for the latest release in a GitHub repository.
    """
    # module_args: Dict[str, Dict[str, Any]] = {
    #     "github_repo": {"type": "str", "required": True},
    #     "github_token": {"type": "str", "required": False},
    #     "github_api_url": {"type": "str", "required": False, "default": "https://api.github.com"},
    #     "prefix": {"type": "str", "required": False},
    #     "suffix": {"type": "str", "required": False},
    #     "contains": {"type": "str", "required": False},
    #     "max_pages": {"type": "int", "required": False, "default": 100},
    #     "timeout": {"type": "int", "required": False, "default": 10},
    # }
    #
    # result = {"changed": False, "original_message": ""}

    # tag_version = github_release_search(
    #     github_repo=module.params["github_repo"],
    #     github_token=module.params["github_token"],
    #     github_api_url=module.params["github_api_url"],
    #     prefix=module.params["prefix"],
    #     suffix=module.params["suffix"],
    #     contains=module.params["contains"],
    #     max_pages=module.params["max_pages"],
    #     timeout=module.params["timeout"],
    # )

    # result["tag_version"] = tag_version
    #
    # module.exit_json(**result)


display = Display()


class LookupModule(LookupBase):
    """
    Lookup module that retrieves version details.
    """

    def run(self, terms: List[str], variables: Optional[Dict[str, Any]] = None, **kwargs: Dict[str, Any]) -> List[str]:
        """
        Run the lookup module.
        """
        if not variables or not variables.get("ansible_facts"):
            raise AnsibleLookupError(
                "ansible_facts/ansible_architecture is expected,"
                "make sure ansible_facts/ansible_architecture is present"
            )

        self.set_options(var_options=variables, direct=kwargs)

        if not terms:
            raise AnsibleLookupError("No terms provided for lookup")

        if len(terms) > 1:
            raise AnsibleLookupError(f"Only one term is allowed for lookup, got {len(terms)}, {terms}")
        version_details: VersionDetails
        try:
            version_details = get_version(
                ansible_architecture=str(variables.get("ansible_architecture")), app_name=terms[0]
            )
        except Exception as e:
            raise AnsibleLookupError(f"Failed to get version details for {terms[0]}: {e}") from e

        return [json.dumps(asdict(version_details))]
