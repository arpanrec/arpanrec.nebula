# Ansible Role: NodeJS (arpanrec.nebula.nodejs)

## NodeJS

Install NodeJS in user space

## Variable

- `nodejs_rv_install_path`

  - Description: Install path for nodejs.
  - Default: `"{{ ansible_facts.user_dir }}/.local/share/node"`
  - Required: `false`
  - Type: `str`

- `nodejs_rv_version`

  - Description:
    - Release version.
    - If set to `fetch_latest_version`, it will fetch the latest version from [Github](https://github.com/nodejs/node/releases).
  - Default: `v20.13.1`
  - Required: `false`
  - Type: `str`
  - Default: `fetch_latest_version`

- `nodejs_rv_tmp_install_cache_dir`

  - Description: Cache install directory.
  - Default: `"{{ ansible_facts.user_dir }}/.tmp/nodejs"`
  - Required: `false`
  - Type: `str`

### Example Playbook NodeJS

```yaml
- name: Include NodeJS
  ansible.builtin.import_role:
      name: arpanrec.nebula.nodejs
```

### Testing NodeJS

```bash
molecule test -s role.nodejs.default
```
