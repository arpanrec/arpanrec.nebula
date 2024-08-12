#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build dynamic inventory from HashiCorp Vault KV2 secrets engine.

Author: Arpan Mandal
Requirements: Python 3 or higher
"""
import json
import os
from collections.abc import MutableMapping  # type: ignore
from typing import Dict

import hvac  # type: ignore
import yaml
from ansible.errors import AnsibleError, AnsibleParserError  # type: ignore
from ansible.inventory.data import InventoryData  # type: ignore
from ansible.module_utils.common.text.converters import to_text  # type: ignore
from ansible.module_utils.six import string_types  # type: ignore
from ansible.parsing.dataloader import DataLoader  # type: ignore
from ansible.plugins.inventory import BaseFileInventoryPlugin  # type: ignore
from hvac.exceptions import InvalidPath  # type: ignore

DOCUMENTATION = r"""
    name: hashicorp_vault_kv2_inventory
    author:
        - Arpan Mandal
    requirements:
        - python >= 3.10
    description:
        - This plugin allows users to use HashiCorp Vault as a dynamic inventory source.
    extends_documentation_fragment:
        - constructed
    options:
        plugin:
            description: Name of the plugin
            required: true
            choices: ["hashicorp_vault_kv2_inventory"]
            type: str
            default: hashicorp_vault_kv2_inventory
        hvac_client_configuration:
            description:
                - Configuration for the HashiCorp Vault client.
                - Configuration options are the same as the options for the hvac.Client class.
                - https://hvac.readthedocs.io/en/stable/source/hvac_v1.html#hvac.v1.Client
                - If starting with '@', the value is treated as a file path and the content is read from the file.
            required: true
            type: dict
        hvac_client_auth_method:
            description:
                - Authentication method for the HashiCorp Vault client.
                - Supported authentication methods are: userpass, approle.
                - In case of token authentication, it can be set directly in the hvac_client_configuration.
                - If starting with '@', the value is treated as a file path and the content is read from the file.
            required: false
            type: str
            default: userpass
            choices: ["userpass", "approle"]
        hvac_client_auth_config:
            description:
                - Configuration for the HashiCorp Vault client authentication method.
                - If starting with '@', the value is treated as a file path and the content is read from the file.
            required: false
            type: dict
        hvac_kv2_mount_point:
            description:
                - Path to the KV version 2 secrets engine mount point.
                - If starting with '@', the value is treated as a file path and the content is read from the file.
            required: false
            type: str
            default: secret
        hvac_kv2_path:
            description:
                - Path to the KV version 2 secrets engine path.
                - If starting with '@', the value is treated as a file path and the content is read from the file.
            required: false
            type: str
            default: ansible_inventory
        add_hvac_client_to_inventory:
            description: Add HashiCorp Vault client configuration to the inventory.
            required: false
            type: bool
            default: false
"""

NoneType = type(None)


def file_or_string(value):
    """Read a file if the value is a file path, otherwise return the value as is"""
    if value is None:
        return None

    if isinstance(value, Dict):
        return value

    if isinstance(value, str) and value.startswith("@"):
        _, file_extension = os.path.splitext(value[1:])

        if file_extension not in [".json", ".yml", ".yaml"]:
            raise ValueError(f"Unsupported file extension: {file_extension}")

        with open(value[1:], "r", encoding="utf-8") as f:
            if file_extension in [".json"]:
                return json.load(f)
            return yaml.safe_load(f)
    return value


class InventoryModule(BaseFileInventoryPlugin):
    """
    Ansible dynamic inventory plugin for Hashicorp Vault
    """

    # used internally by Ansible, it should match the file name but not required
    NAME = "hashicorp_vault_kv2_inventory"

    hvac_client: hvac.Client
    hvac_kv2_mount_point: str

    def parse(self, inventory: InventoryData, loader: DataLoader, path, cache=False):
        """parse and populate the inventory with data"""

        super().parse(inventory, loader, path)
        # self.set_options()

        try:
            ansible_inventory_dict = loader.load_from_file(path, cache=cache)
        except Exception as e:
            raise AnsibleParserError(f"Unable to parse {path} as YAML: {to_text(e)}") from e

        hvac_client_configuration = file_or_string(ansible_inventory_dict.get("hvac_client_configuration", {}))
        hvac_client_auth_method = file_or_string(ansible_inventory_dict.get("hvac_client_auth_method", None))
        hvac_client_auth_config = file_or_string(ansible_inventory_dict.get("hvac_client_auth_config", {}))
        self.hvac_kv2_mount_point = file_or_string(ansible_inventory_dict.get("hvac_kv2_mount_point", "secret"))
        hvac_kv2_path = file_or_string(ansible_inventory_dict.get("hvac_kv2_path", "ansible_inventory"))

        if hvac_kv2_path.startswith("/") or hvac_kv2_path.endswith("/"):
            raise AnsibleParserError(
                f"Invalid HashiCorp Vault KV2 path: {hvac_kv2_path}. Path should not start or end with a forward slash"
            )

        if "cert" in hvac_client_configuration.keys():
            cert_list: list = hvac_client_configuration["cert"]
            hvac_client_configuration["cert"] = tuple(cert_list)

        self.hvac_client = hvac.Client(**hvac_client_configuration)

        if hvac_client_auth_method and hvac_client_auth_method not in [
            "userpass",
            "approle",
        ]:
            raise ValueError(f"Unsupported authentication method: {hvac_client_auth_method}")

        if "userpass" == hvac_client_auth_method:
            try:
                self.hvac_client.auth.userpass.login(**hvac_client_auth_config)
            except Exception as e:
                raise AnsibleParserError(f"Error authenticating with userpass: {to_text(e)}") from e

        if "approle" == hvac_client_auth_method:
            try:
                self.hvac_client.auth.approle.login(**hvac_client_auth_config)
            except Exception as e:
                raise AnsibleParserError(f"Error authenticating with approle: {to_text(e)}") from e

        ansible_inventory: InventoryData = self.inventory

        if ansible_inventory_dict.get("add_hvac_client_to_inventory", False):
            ansible_inventory.set_variable(
                "all",
                "hashicorp_vault_kv2_inventory",
                {
                    "hvac_client_configuration": hvac_client_configuration,
                    "hvac_client_auth_method": hvac_client_auth_method,
                    "hvac_client_auth_config": hvac_client_auth_config,
                    "hvac_kv2_mount_point": self.hvac_kv2_mount_point,
                    "hvac_kv2_path": hvac_kv2_path,
                    "hvac_token": self.hvac_client.token,
                },
            )

        config = {"all": self.read_from_vault(hvac_kv2_path)}
        config = loader.load(data=yaml.dump(config), show_content=True)
        self.display.vvvvvv(f"Config: {json.dumps(config, indent=4)}")
        for group_name in config:  # type: ignore
            self._parse_group(group_name, config[group_name])

    def _parse_group(self, group, group_data):  # pylint: disable=too-many-branches

        if isinstance(group_data, (MutableMapping, NoneType)):  # type: ignore[misc]

            try:
                group = self.inventory.add_group(group)
            except AnsibleError as e:
                raise AnsibleParserError(f"Unable to add group {group}: {to_text(e)}") from e

            if group_data is not None:
                # make sure they are dicts
                for section in ["vars", "children", "hosts"]:
                    if section in group_data:
                        # convert strings to dicts as these are allowed
                        if isinstance(group_data[section], string_types):
                            group_data[section] = {group_data[section]: None}

                        if not isinstance(group_data[section], (MutableMapping, NoneType)):  # type: ignore[misc]
                            raise AnsibleParserError(
                                f"Invalid {section} entry for {group} group,"
                                "requires a dictionary, found {type(group_data[section])}"
                            )

                for key in group_data:

                    if not isinstance(group_data[key], (MutableMapping, NoneType)):  # type: ignore[misc]
                        self.display.warning(
                            f"Skipping key ({key}) in group ({group})"
                            "as it is not a mapping, it is a {type(group_data[key])}"
                        )
                        continue

                    if isinstance(group_data[key], NoneType):  # type: ignore[misc]
                        self.display.vvv(f"Skipping empty key ({key}) in group ({group})")
                    elif key == "vars":
                        for var in group_data[key]:
                            self.inventory.set_variable(group, var, group_data[key][var])
                    elif key == "children":
                        for subgroup in group_data[key]:
                            subgroup = self._parse_group(subgroup, group_data[key][subgroup])
                            self.inventory.add_child(group, subgroup)

                    elif key == "hosts":
                        for host_pattern in group_data[key]:
                            hosts, port = self._parse_host(host_pattern)
                            self._populate_host_vars(hosts, group_data[key][host_pattern] or {}, group, port)
                    else:
                        self.display.warning(
                            f"Skipping unexpected key ({key}) in group ({group}),"
                            "only vars, children and hosts are valid"
                        )

        else:
            self.display.warning(f"Skipping {group} as this is not a valid group definition")

        return group

    def _parse_host(self, host_pattern):
        """
        Each host key can be a pattern, try to process it and add variables as needed
        """
        try:
            (hostnames, port) = self._expand_hostpattern(host_pattern)
        except TypeError as e:
            raise AnsibleParserError(
                f"Host pattern {host_pattern} must be a string. Enclose integers/floats in quotation marks."
            ) from e
        return hostnames, port

    def _filter_null_from_vault(self, data):
        """Filter out null values from HashiCorp Vault"""
        if data is None:
            return None
        if isinstance(data, (str)):
            if isinstance(data, str) and (len(data) == 0 or data == ""):
                return None
            return data
        return data

    def read_from_vault(self, path):
        """Read data from HashiCorp Vault"""
        config = {}

        try:
            read_secret_version = self.hvac_client.secrets.kv.v2.read_secret_version(
                path=path, mount_point=self.hvac_kv2_mount_point
            )
            if read_secret_version["data"]["data"]:
                for key, value in read_secret_version["data"]["data"].items():
                    config[key] = self._filter_null_from_vault(value)
        except InvalidPath as e:
            self.display.vvv(f"Ignoring invalid path in HashiCorp Vault: {e}.")
        except Exception as e:
            self.display.error(f"Error reading from HashiCorp Vault: {e}")
            raise AnsibleParserError("Error reading from HashiCorp Vault.") from e

        try:
            list_secrets = self.hvac_client.secrets.kv.v2.list_secrets(path=path, mount_point=self.hvac_kv2_mount_point)
            for key in list_secrets["data"]["keys"]:

                if key.endswith("/"):
                    key = key[:-1]

                if key in config:
                    self.display.error(f"Duplicate key found in HashiCorp Vault: {key} in {path}")
                    raise AnsibleParserError(f"Duplicate key found in HashiCorp Vault: {key} in {path}")

                list_config = self.read_from_vault(f"{path}/{key}")
                config[key] = list_config

        except InvalidPath as e:
            self.display.vvv(f"Ignoring invalid path in HashiCorp Vault: {e}")
        except Exception as e:
            self.display.error(f"Error reading from HashiCorp Vault: {e}")
            raise AnsibleParserError(f"Error reading from HashiCorp Vault: {e}") from e

        return config
