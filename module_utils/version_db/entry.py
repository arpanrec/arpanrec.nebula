#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
from ansible.module_utils.basic import AnsibleModule

from . import SUPPORTED_APPS


def run_module():
    module_args = dict(
        name=dict(type='str', required=False),
        new=dict(type='bool', required=False, default=False)
    )

    module = AnsibleModule(
        argument_spec=module_args,
    )
    module.exit_json(**SUPPORTED_APPS)
