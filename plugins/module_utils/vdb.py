import requests
from ansible.module_utils.basic import AnsibleModule


def get_version():
    module_args = dict(
        name=dict(type='str', required=False),
        new=dict(type='bool', required=False, default=False)
    )

    module = AnsibleModule(
        argument_spec=module_args,
    )
    module.exit_json(**{"SUPPORTED_APPS": 123})
