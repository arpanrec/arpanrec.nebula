# Ansible Collection Nebula (arpanrec.nebula)

## Description

This collection provides a set of roles to deploy and manage various services.

## Roles

- [Bitwarden Desktop](/roles/bitwarden_desktop/README.md)
- [Secrets Manager CLI](/roles/bws/README.md)
- [Visual Studio Code](/roles/code/README.md)
- [Get Certificate from ownca](/roles/get_certificate_ownca/README.md)
- [GNOME](/roles/gnome/README.md)
- [The Go Programming Language](/roles/go/README.md)
- [Java](/roles/java/README.md)
- [linux_patching](/roles/linux_patching/README.md)
- [Mattermost Desktop](/roles/mattermost_desktop/README.md)
- [NodeJS](/roles/nodejs/README.md)
- [Postman](/roles/postman/README.md)
- [ssh_hardening](/roles/ssh_hardening/README.md)
- [Telegram Desktop](/roles/telegram_desktop/README.md)
- [Terraform by HashiCorp](/roles/terraform/README.md)
- [themes](/roles/themes/README.md)
- [terminal](/roles/terminal/README.md)
- [user_add](/roles/user_add/README.md)
- [utils](/roles/utils/README.md)
- [Vault by HashiCorp](/roles/vault/README.md)
- [Pulumi](/roles/pulumi/README.md)

## Playbooks

- [server_workspace](/playbooks/server_workspace.md)
- [cloudinit](/playbooks/cloudinit.md)

## Installation

```bash
export NEBULA_VERSION=1.10.8
curl "https://raw.githubusercontent.com/arpanrec/arpanrec.nebula/refs/tags/${NEBULA_VERSION}/requirements.yml" \
    -o "/tmp/requirements-${NEBULA_VERSION}.yml"
ansible-galaxy install -r "/tmp/requirements-${NEBULA_VERSION}.yml"
ansible-galaxy collection install "git+https://github.com/arpanrec/arpanrec.nebula.git,${NEBULA_VERSION}"
```

## [License](LICENSE)

`GLWTS`

Visit [GLWTS Public License](https://raw.githubusercontent.com/me-shaon/GLWTPL/master/NSFW_LICENSE) for more information.
