#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ansible secret lookup plugin for retrieving secrets from Vault.
"""

from __future__ import absolute_import, division, print_function

from typing import Any, Dict, List, Optional, Union

from ansible.errors import AnsibleLookupError  # type: ignore
from ansible.plugins.lookup import LookupBase  # type: ignore
from ansible.utils.display import Display  # type: ignore

# pylint: disable=import-error,E0611
from ansible_collections.arpanrec.nebula.plugins.module_utils.cryptpass import cryptpass_client  # type: ignore

__metaclass__ = type  # pylint: disable=invalid-name
display = Display()

# pylint: disable=duplicate-code
DOCUMENTATION = r"""
name: arpanrec.nebula.cryptpass
version_added: "0.1.0"
short_description: Read secrets from the cryptpass secrets service.
description:
    - This lookup plugin retrieves secrets from the cryptpass secrets service.
options:
    _terms:
        description: The secret key to retrieve.
        required: true
    config:
        description:
            - Executes the specified action (read, write, list, delete) on the secret identified by the key.
            - Environment variable CRYPTPASS_CLIENT_CONFIG can be used to set the configuration file path \
              or JSON string.
            - If not set, it defaults to ~/.cryptpass_client.json.
            - |+
                The config file or JSON string must contain the following
                ```json
                {
                    "endpoint": "https://127.0.0.1:8080",
                    "headers": {
                        "X-CRYPTPASS-KEY": "auth_token"
                    },
                    "ca_cert_pem": "Content of the CA PEM certificate file"
                }
                ```
        ini:
            - section: cryptpass
              key: config
author:
    - Arpan Mandal (mailto:arpan.rec@gmail.com)
"""

EXAMPLES = r"""
- name: Retrieve a secret from Vault
  ansible.builtin.debug:
      msg: "{{ lookup('arpanrec.nebula.cryptpass', 'project/key') }}"
"""


class LookupModule(LookupBase):
    """
    LookupModule is a custom Ansible lookup plugin for retrieving secrets from Vault.
    Methods:
        run(
            terms: List[str], variables: Optional[Dict[str, Any]] = None, **kwargs: Optional[Dict[str, Any]]
        ) -> List[str]:
            Executes the lookup plugin with the provided terms and variables.
    Raises:
        AnsibleError: If the number of terms provided is not exactly one.
    Returns:
        List[str]: A list containing the single term provided.
    """

    def run(
        self, terms: List[str], variables: Optional[Dict[str, Any]] = None, **kwargs: Optional[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:

        self.set_options(var_options=variables, direct=kwargs)

        if len(terms) != 1:
            raise AnsibleLookupError(f"cryptpass lookup expects a 1 argument but got {len(terms)}")
        config: Optional[Union[Dict[str, str] | str]] = None

        if self.get_option("config"):
            config = self.get_option("config")

        if not config and variables and "cryptpass_lookup_config" in variables:
            config = variables["cryptpass_lookup_config"]

        key: str = terms[0]

        try:
            data = cryptpass_client(key=key, action="read", value=None, config=config)["secret"]
        except ValueError as e:
            raise AnsibleLookupError(f"Error retrieving secret: {e}") from e

        return [data]
