# Ansible Role: Terraform (arpanrec.nebula.terraform)

## Terraform

Install Terraform in user space

## Variable

- `terraform_rv_install_path`

  - Description: Install path for terraform.
  - Default: `"{{ ansible_facts.user_dir }}/.local/bin"`
  - Required: `false`
  - Type: `str`

- `terraform_rv_version`

  - Description:
    - Terraform version to install.
    - If set to `fetch_latest_version`, it will fetch the latest release from the api. Get latest release from [releases](https://releases.hashicorp.com/terraform/index.json).
    - Example `1.0.9`.
  - Required: `false`.
  - Default: `fetch_latest_version`.
  - Type: `str`.

- `terraform_rv_tmp_install_cache_dir`

  - Description: Cache install directory.
  - Default: `"{{ ansible_facts.user_dir }}/.tmp/terraform"`.
  - Required: `false`.
  - Type: `str`.

### Example Playbook Terraform

```yaml
- name: Include Terraform
  ansible.builtin.import_role:
      name: arpanrec.nebula.terraform
```

### Testing Terraform

```bash
molecule test -s role.terraform.default
```
