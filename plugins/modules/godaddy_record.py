# -*- coding: utf-8 -*-
"""
Ansible module to manage GoDaddy DNS Records
"""

from ansible.module_utils.basic import AnsibleModule  # type: ignore
from godaddypy import Client, Account  # type: ignore

ANSIBLE_METADATA = {"metadata_version": "1.1", "status": ["preview"], "supported_by": "community"}

DOCUMENTATION = """
---
module: arpanrec.nebula.godaddy_record

short_description: Manage Godaddy DNS Records

version_added: "2.4"

description:
    - "Create, delete and update GoDaddy DNS Records"

options:
    api_key:
        description: GoDaddy API Key
        required: true
    api_secret:
        description: GoDaddy API Secret
        required: true
    domain:
        description: Domain name
        required: true
    name:
        description: Record name
        required: true
    type:
        description: Record type
        required: false
        choices: ["A", "AAAA", "CNAME", "SRV", "TXT", "SOA", "NS", "MX", "SPF", "PTR"]
        default: "A"
    data:
        description: Record data
        required: true
    ttl:
        description: Record TTL
        required: false
        default: 600
    state:
        description: Record state
        required: false
        choices: ["present", "absent"]
        default: "present"
author:
    - Arpan Mandal
"""

EXAMPLES = """
---
# Update A Record
- name: Test with a message
  godaddy_record:
      name: mail
      type: A
"""

RETURN = """
---
original_message:
    description: The original name param that was passed in
    type: str
    returned: always
message:
    description: The output message that the test module generates
    type: str
    returned: always
"""


SUPPORTED_RECORD_TYPES = ["A", "AAAA", "CNAME", "SRV", "TXT", "SOA", "NS", "MX", "SPF", "PTR"]


def run_module():
    """
    Run the module
    """
    # define available arguments/parameters a user can pass to the module
    module_args = {
        "api_key": {"type": "str", "required": True, "no_log": True},
        "api_secret": {"type": "str", "required": True, "no_log": True},
        "domain": {"type": "str", "required": True},
        "name": {"type": "str", "required": True},
        "type": {"type": "str", "required": False, "choices": SUPPORTED_RECORD_TYPES, "default": "A"},
        "data": {"type": "str", "required": True},
        "ttl": {"type": "int", "required": False, "default": 600},
        "state": {"type": "str", "required": False, "choices": ["present", "absent"], "default": "present"},
    }
    result = {"changed": False}

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    client = Client(Account(api_key=module.params["api_key"], api_secret=module.params["api_secret"]))

    domain = module.params["domain"]
    t = module.params["type"]
    name = module.params["name"]
    ttl = module.params["ttl"]
    data = module.params["data"]

    recs = client.get_records(domain, record_type=t, name=name)
    if len(recs) == 0:
        client.add_record(domain, {"data": data, "name": name, "ttl": ttl, "type": t})
        result["changed"] = True
    else:
        rec = recs[0]
        if rec["data"] != data or rec["ttl"] != ttl:
            rec["data"] = data
            rec["ttl"] = ttl
            client.update_record(domain, {"data": data, "name": name, "ttl": ttl, "type": t})
            result["changed"] = True
    if module.check_mode:
        module.exit_json(**result)

    module.exit_json(**result)


def main():
    """
    Main function
    """
    run_module()


if __name__ == "__main__":
    main()
