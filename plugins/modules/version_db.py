#!/usr/bin/env python3


from __future__ import absolute_import, division, print_function

from typing import Any, Dict

from ansible.module_utils.basic import AnsibleModule  # type: ignore
from ansible.module_utils.vdb import get_version

# pylint: disable=C0103,invalid-name
__metaclass__ = type


def run_module() -> None:
    """
    Search for the latest release in a GitHub repository.
    """
    module_args: Dict[str, Dict[str, Any]] = {}

    result = {"changed": False, "original_message": ""}

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    tag_version = get_version()

    result["tag_version"] = tag_version

    module.exit_json(**result)


def main() -> None:
    """
    Python Main Module
    """
    run_module()


if __name__ == "__main__":
    main()
