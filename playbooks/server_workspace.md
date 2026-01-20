# [Ansible Play Server Workspace](/playbooks/server_workspace.yml)

Run the playbook

## Hosts

- server_workspace

This playbook is designed to run on the server or group named `server_workspace` in your Ansible inventory.

## Extra Vars

Extra variables will be applied to the original role.

## Tags

### Enabled by Default

- [Node JS](../roles/nodejs/README.md) -> nodejs
- [Go Language](../roles/go/README.md) -> go
- [Oracle JDK](../roles/java/README.md) -> java
- [Terminal Themes](../roles/terminal/README.md) -> terminal

### Disabled by Default

- [Themes](../roles/themes/README.md) -> themes
