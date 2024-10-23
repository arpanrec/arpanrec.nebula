# Ansible Role: Vault (arpanrec.nebula.vault)

## Hashicorp Vault

Install Hashicorp Vault in user space

## Variable

- `vault_rv_install_path`

  - Description: Install path for vault.
  - Default: `"{{ ansible_facts.user_dir }}/.local/bin"`
  - Required: `false`
  - Type: `str`

- `vault_rv_version`

  - Description:
    - Vault Release version.
    - If set to `fetch_latest_version`, it will fetch the latest release from the api. Get latest release from [releases](https://releases.hashicorp.com/vault/index.json).
    - Example `1.16.2`.
  - Required: `false`.
  - Default: `fetch_latest_version`.
  - Type: `str`.

- `vault_rv_tmp_install_cache_dir`

  - Description: Cache install directory.
  - Default: `"{{ ansible_facts.user_dir }}/.tmp/vault"`
  - Required: `false`
  - Type: `str`

### Example Playbook Vault

```yaml
- name: Include Vault
  ansible.builtin.import_role:
      name: arpanrec.nebula.vault
```

### Testing Vault

```bash
molecule test -s role.vault.default
```
