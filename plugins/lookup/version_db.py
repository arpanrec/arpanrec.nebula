#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Ansible Module for Search for the latest release in a GitHub repository.
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type  # pylint: disable=invalid-name

import json
from dataclasses import asdict
from typing import Any, Dict, List, Optional

from ansible.errors import AnsibleLookupError  # type: ignore
from ansible.plugins.lookup import LookupBase  # type: ignore
from ansible.utils.display import Display  # type: ignore

# pylint: disable=import-error,no-name-in-module
from ansible_collections.arpanrec.nebula.plugins.module_utils.version_db import get_version  # type: ignore
from ansible_collections.arpanrec.nebula.plugins.module_utils.version_db.models import VersionDetails  # type: ignore

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
            description: The app name.
            required: true
            type: str
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

        self.set_options(var_options=variables, direct=kwargs)

        if not terms:
            raise AnsibleLookupError("No terms provided for lookup")

        if len(terms) > 1:
            raise AnsibleLookupError(f"Only one term is allowed for lookup, got {len(terms)}, {terms}")

        version_details: VersionDetails
        try:
            version_details = get_version(app_name=terms[0], variables=variables, **kwargs)
        except Exception as e:
            raise AnsibleLookupError(f"Failed to get version details for {terms[0]}: {str(e)}") from e

        return [json.dumps(asdict(version_details))]  # type: ignore
