# [Ansible Play Server Workspace](server_workspace.yml)

Run the playbook

## Hosts

* server_workspace

This playbook is designed to run on the server or group named `server_workspace` in your Ansible inventory.

## Extra Vars

Extra variables will be applied to the original role.

## Tags

### Enabled by Default

* [Dot Files](../roles/dotfiles/README.md) -> dotfiles
* [Node JS](../roles/nodejs/README.md) -> nodejs
* [Go Language](../roles/go/README.md) -> go
* [Oracle JDK](../roles/java/README.md) -> java
* [terminal](../roles/terminal/README.md) -> terminal
* [Terraform](../roles/terraform/README.md) -> terraform
* [Vault](../roles/vault/README.md) -> vault

### Disabled by Default

* [Bitwarden Desktop](../roles/bitwarden_desktop/README.md) -> bitwarden_desktop
* [Mattermost Desktop](../roles/mattermost_desktop/README.md) -> mattermost_desktop
* [Telegram Desktop](../roles/telegram_desktop/README.md) -> telegram_desktop
* [Postman](../roles/postman/README.md) -> postman
* [Microsoft Visual Studio Code](../roles/code/README.md) -> code
* [Gnome Settings](../roles/gnome/README.md) -> gnome
* [Themes](../roles/themes/README.md) -> themes
