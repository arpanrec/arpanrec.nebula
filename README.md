# Ansible Collection Nebula (arpanrec.nebula)

## Description

This collection provides a set of roles to deploy and manage various services.

## Roles

- [The Go Programming Language](/roles/go/README.md)
- [Java](/roles/java/README.md)
- [linux_patching](/roles/linux_patching/README.md)
- [NodeJS](/roles/nodejs/README.md)
- [ssh_hardening](/roles/ssh_hardening/README.md)
- [themes](/roles/themes/README.md)
- [terminal](/roles/terminal/README.md)
- [user_add](/roles/user_add/README.md)
- [Gitea](/roles/gitea/README.md)
- [Postgresql](/roles/postgresql/README.md)

## Playbooks

- [server_workspace](/playbooks/server_workspace.md)
- [cloudinit](/playbooks/cloudinit.md)

## Plugins

### Lookups

    - [version_db](/plugins/lookup/version_db.py)

### Filters

    - [split_certificates](/plugins/filter/split_certificates.py)

## Installation

    ```bash
    export NEBULA_VERSION=1.11.0
    curl "https://raw.githubusercontent.com/arpanrec/arpanrec.nebula/refs/tags/${NEBULA_VERSION}/requirements.yml" \
        -o "/tmp/requirements-${NEBULA_VERSION}.yml"
    ansible-galaxy install -r "/tmp/requirements-${NEBULA_VERSION}.yml"
    ansible-galaxy collection install "git+https://github.com/arpanrec/arpanrec.nebula.git,${NEBULA_VERSION}"
    ```

## [License](LICENSE)

`MIT`
