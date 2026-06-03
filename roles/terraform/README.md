# Ansible Role: Terraform (arpanrec.nebula.terraform)

Installs the [HashiCorp Terraform](https://www.terraform.io/) CLI in user space for infrastructure-as-code provisioning and management.

## Features

- User-space installation (no root privileges required)
- Automatic latest-version detection via the HashiCorp Releases API
- Configurable installation and cache directories

## Requirements

- Debian-based Linux distribution
- `unzip` available on the target host

## Variables

| Variable                             | Type  | Required | Default                                       | Example | Description                                                                                                            |
| ------------------------------------ | ----- | -------- | --------------------------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------- |
| `terraform_rv_install_path`          | `str` | `false`  | `{{ ansible_facts.user_dir }}/.local/bin`     | -       | Directory where the `terraform` binary is placed.                                                                      |
| `terraform_rv_version`               | `str` | `false`  | `fetch_latest_version`                        | `1.9.0` | Version to install. Set to `fetch_latest_version` to resolve the latest from the HashiCorp Releases API automatically. |
| `terraform_rv_tmp_install_cache_dir` | `str` | `false`  | `{{ ansible_facts.user_dir }}/.tmp/terraform` | -       | Temporary directory used during download and extraction.                                                               |

## Example Playbook

```yaml
- name: Install Terraform
  hosts: all
  roles:
      - name: arpanrec.nebula.terraform
```

Pin a specific version:

```yaml
- name: Install Terraform
  hosts: all
  roles:
      - name: arpanrec.nebula.terraform
        vars:
            terraform_rv_version: '1.9.0'
```

## Testing

```bash
molecule test -s role.terraform.default
```
