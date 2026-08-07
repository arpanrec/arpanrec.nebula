# [Ansible Play Cloud Init](/playbooks/cloudinit.yml)

Run the playbook

## Hosts

- cloudinit

This playbook is designed to run on the server or group named `cloudinit` in your Ansible inventory.

## Extra Vars

All of the variables below are required; the playbook fails early if any of them is missing.
Extra variables will be applied to the original role.

`pv_cloud_init_group` - The name of the primary group to create for the application user.

`pv_cloud_init_user` - The username of the application user to create.

`pv_cloud_init_authorized_keys` - The path to a local file containing the SSH public keys (one per line) to authorize for the application user.

`pv_cloud_init_is_dev_machine` - Whether the machine is a development machine or not. When `true`, development packages are installed by [linux_patching](../roles/linux_patching/README.md).

`pv_cloud_init_hostname` - The hostname to set on the machine.

`pv_cloud_init_domain` - The domain name to set on the machine.

`pv_cloud_init_install_docker` - Whether to install Docker on the machine (via the `geerlingguy.docker` role).
