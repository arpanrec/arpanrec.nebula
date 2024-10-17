# -*- coding: utf-8 -*-
"""
Ansible Module for Search for the latest release in a GitHub repository.
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from typing import List, Dict, Any, Optional

from ansible.errors import AnsibleLookupError  # type: ignore
from ansible.plugins.lookup import LookupBase  # type: ignore
from ansible.utils.display import Display  # type: ignore

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
        e_search:
            description:
                - Field to retrieve, for example V(name) or V(id).
                - If set to V(id), only zero or one element can be returned.
                  Use the Jinja C(first) filter to get the only list element.
                - If set to V(None) or V(''), or if O(_terms) is empty, records are not filtered by fields.
            type: str
            version_added: 5.7.0
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

        self.set_options(var_options=variables, direct=kwargs)

        if not terms:
            raise AnsibleLookupError("No terms provided for lookup")

        if len(terms) > 1:
            raise AnsibleLookupError(f"Only one term is allowed for lookup, got {len(terms)}, {terms}")

        for term in terms:
            display.debug("File lookup term: %s" % term)
            display.v("File lookup term: %s" % term)
        display.v("Variables: %s" % self.get_option("e_search"))

        return ["ret", "sfasf,safas"]
