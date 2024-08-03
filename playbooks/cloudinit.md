# [Ansible Play Cloud Init](/playbooks/cloudinit.yml)

Run the playbook

## Hosts

* cloud_init

This playbook is designed to run on the server or group named `cloud_init` in your Ansible inventory.

## Extra Vars

Extra variables will be applied to the original role.

`pv_cloud_init_group` - The name of the group to create in the cloud provider.

`pv_cloud_init_user` - The username to use for the cloud provider.

`pv_cloud_init_authorized_keys` - The path to the file containing the public keys to use for the cloud provider.

`pv_cloud_init_is_dev_machine` - Whether the machine is a development machine or not.

`pv_cloud_init_hostname` - The hostname to use for the cloud provider.

`pv_cloud_init_domain` - The domain to use for the cloud provider.
