# Ansible Role: Vault (arpanrec.nebula.vault)

Installs the [HashiCorp Vault](https://www.vaultproject.io/) CLI in user space. Vault provides secure storage and access to secrets, encryption keys, and sensitive data.

## Features

- User-space installation (no root privileges required)
- Automatic latest-version detection via the HashiCorp Releases API
- Configurable installation and cache directories

## Requirements

- Debian-based Linux distribution
- `unzip` available on the target host

## Variables

| Variable                         | Type  | Required | Default                                   | Example  | Description                                                                                                            |
| -------------------------------- | ----- | -------- | ----------------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------- |
| `vault_rv_install_path`          | `str` | `false`  | `{{ ansible_facts.user_dir }}/.local/bin` | -        | Directory where the `vault` binary is placed.                                                                          |
| `vault_rv_version`               | `str` | `false`  | `fetch_latest_version`                    | `1.16.2` | Version to install. Set to `fetch_latest_version` to resolve the latest from the HashiCorp Releases API automatically. |
| `vault_rv_tmp_install_cache_dir` | `str` | `false`  | `{{ ansible_facts.user_dir }}/.tmp/vault` | -        | Temporary directory used during download and extraction.                                                               |

## Example Playbook

```yaml
- name: Install Vault CLI
  hosts: all
  roles:
      - name: arpanrec.nebula.vault
```

Pin a specific version:

```yaml
- name: Install Vault CLI
  hosts: all
  roles:
      - name: arpanrec.nebula.vault
        vars:
            vault_rv_version: '1.16.2'
```

## Testing

```bash
molecule test -s role.vault.default
```
