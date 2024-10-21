#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Ansible Module for Search for the latest release in a GitHub repository.
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import json
from dataclasses import asdict
from typing import Any, Dict, List, Optional

from ansible.errors import AnsibleLookupError  # type: ignore
from ansible.plugins.lookup import LookupBase  # type: ignore
from ansible.utils.display import Display  # type: ignore
from ansible_collections.arpanrec.nebula.plugins.module_utils.version_db import VersionDetails, get_version

DOCUMENTATION = """
---
    name: version_db
    author:
        - Arpan Mandal <me@arpanrec.com>
    short_description: Get version details.
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


display = Display()


class LookupModule(LookupBase):
    """
    Lookup module that retrieves version details.
    """

    def run(self, terms: List[str], variables: Optional[Dict[str, Any]] = None, **kwargs: Dict[str, Any]) -> List[str]:
        """
        Run the lookup module.
        """
        # if not variables or not variables.get("ansible_facts"):
        #     raise AnsibleLookupError(
        #         "ansible_facts/ansible_architecture is expected,"
        #         "make sure ansible_facts/ansible_architecture is present"
        #     )

        self.set_options(var_options=variables, direct=kwargs)

        if not terms:
            raise AnsibleLookupError("No terms provided for lookup")

        if len(terms) > 1:
            raise AnsibleLookupError(f"Only one term is allowed for lookup, got {len(terms)}, {terms}")

        version_details: VersionDetails
        try:
            version_details = get_version(app_name=terms[0], variables=variables, **kwargs)
        except Exception as e:
            raise AnsibleLookupError(f"Failed to get version details for {terms[0]}: {e}") from e

        return [json.dumps(asdict(version_details))]
