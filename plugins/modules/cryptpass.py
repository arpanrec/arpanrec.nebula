#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ansible Module for managing secrets.
"""

# Copyright: (c) 2022, Arpan Mandal <arpan.rec@gmail.com>
# MIT (see LICENSE or https://en.wikipedia.org/wiki/MIT_License)
from __future__ import absolute_import, division, print_function

from ansible.module_utils.basic import AnsibleModule  # type: ignore

# pylint: disable=import-error,E0611
from ansible_collections.arpanrec.nebula.plugins.module_utils.cryptpass import cryptpass_client  # type: ignore

# pylint: disable=C0103
__metaclass__ = type

# pylint: disable=duplicate-code
DOCUMENTATION = r"""
---
module: arpanrec.nebula.cryptpass

short_description: "Ansible module for managing secrets"

version_added: "1.12.0"

description:
    - Executes the specified action (read, write, list, delete) on the secret identified by the key.
    - "Environment variable CRYPTPASS_CLIENT_CONFIG can be used to set the configuration file path
      or JSON string."
    - If not set, it defaults to ~/.cryptpass_client_config.json.
    - The config file or JSON string must contain the following `{"endpoint":"https://127.0.0.1:8080","headers":{"X-CRYPTPASS-KEY":"auth_token"},"ca_cert_pem":"Content of the CA PEM certificate file"}`
    - Cryptpass docs `https://github.com/cryptpass/cryptpass`
options:
    key:
        description: Key of the secret. Must not start or end with / and cannot be empty.
        required: true
        type: str
    action:
        description: Action to be performed
        required: false
        type: str
        default: "read"
        choices:
            - read
            - write
            - delete
            - list
    value:
        description:
            - Value of the secret to be written or updated.
            - If action is "write", this should be provided.
        required: false
        type: dict
    config:
        description:
            - Configuration for the client. Can be a JSON or a path to a JSON file.
            - Environment variable CRYPTPASS_CLIENT_CONFIG can be used to set the config file path or content.
            - Default config file is ~/.cryptpass_client_config.json
        required: false
        type: dict
author:
    - Arpan Mandal (mailto:arpan.rec@gmail.com)
"""

EXAMPLES = r"""
- name: Create or Update a repository secret
  arpanrec.nebula.cryptpass:
      key: "project/key"
      action: "write"
      value: "my_secret_value"
      config:
          endpoint: "https://secrets.example.com"
          headers:
              "X-CRYPTPASS-KEY": "auth_token"
          cert_pem: "-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE-----"
"""

RETURN = r"""
secret:
    description: The secret value
    type: str | dict
"""


# pylint: disable=inconsistent-return-statements
def run_module() -> None:
    """
    Ansible module to manage secrets using the cryptpass service.
    Cryptpass docs: https://github.com/cryptpass/cryptpass
    """
    module_args = {
        "key": {"type": "str", "required": True},
        "action": {"type": "str", "required": False, "default": "read", "choices": ["read", "write", "list", "delete"]},
        "value": {"required": False, "type": "dict"},
        "config": {"required": False, "type": "dict"},
    }

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)
    key = module.params["key"]
    action = module.params.get("action", "read")
    value = module.params.get("value", None)
    config = module.params.get("config", None)

    try:
        data = cryptpass_client(key, action, value, config)
        module.exit_json(changed=data["changed"], secret=data["secret"])
    except ValueError as e:
        module.fail_json(msg=f"Error retrieving secret: {e}", changed=False)


def main() -> None:
    """
    Python Main Module
    """
    run_module()


if __name__ == "__main__":
    main()
