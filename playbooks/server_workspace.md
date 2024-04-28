# [Ansible Play Server Workspace](server_workspace.yml)

Run the playbook

## Extra Vars

Extra variables will be applied to the original role.

## Tags

### Enabled by Default

- [Dot Files](../roles/dotfiles/README.md) -> dotfiles
- [Bitwarden CLI](../roles/bw/README.md) -> bw
  - This also installs [Node JS](../roles/nodejs/README.md) -> nodejs
- [Go Language](../roles/go/README.md) -> go
- [Oracle JDK](../roles/java/README.md) -> java
- [terminal](../roles/terminal/README.md) -> terminal
- [Terraform](../roles/terraform/README.md) -> terraform
- [Vault](../roles/vault/README.md) -> vault

### Disabled by Default

- [Bitwarden Desktop](../roles/bitwarden_desktop/README.md) -> bitwarden_desktop
- [Mattermost Desktop](../roles/mattermost_desktop/README.md) -> mattermost_desktop
- [Telegram](../roles/telegram/README.md) -> telegram
- [Postman](../roles/postman/README.md) -> postman
- [Microsoft Visual Studio Code](../roles/code/README.md) -> code
- [Gnome Settings](../roles/gnome/README.md) -> gnome
- [Node JS](../roles/nodejs/README.md) -> nodejs
- [Themes](../roles/themes/README.md) -> themes
