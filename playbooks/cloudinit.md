# [Ansible Play Cloud Init](/playbooks/cloudinit.yml)

Run the playbook

## Hosts

* cloud_init

This playbook is designed to run on the server or group named `cloud_init` in your Ansible inventory.

## Extra Vars

Extra variables will be applied to the original role.

`pv_cloud_init_groupname` - The name of the group to create in the cloud provider.
`pv_cloud_init_username` - The username to use for the cloud provider.
`pv_cloud_init_user_ssh_public_key` - The public key to use for the cloud provider.
`pv_cloud_init_is_dev_machine` - Whether the machine is a development machine or not.
`pv_cloud_init_hostname` - The hostname to use for the cloud provider.
`pv_cloud_init_domainname` - The domain to use for the cloud provider.
