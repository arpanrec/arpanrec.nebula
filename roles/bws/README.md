# Ansible Role: Bitwarden CLI (arpanrec.nebula.bw)

## Bitwarden CLI

Install [Bitwarden ClI](https://www.npmjs.com/package/@bitwarden/cli)

Variables:

- `bws_sdk_version_tag`

  - Description:
    - Version of [Bitwarden BWS SDK ClI](https://github.com/bitwarden/sdk/releases).
    - Default Get latest release name from [github](https://api.github.com/repos/bitwarden/sdk/releases/latest)
  - Type: `str`
  - Required: `false`
  - Example: `0.3.1`

- `bws_sdk_bin_dir`

  - Description: Directory to install BWS
  - Type: `str`
  - Required: `false`
  - Default: `{{ ansible_facts.user_dir }}/.local/bin`

- `bws_sdk_tmp_dir`

  - Description: Directory to temporary download BWS.
  - Type: `str`
  - Required: `false`
  - Default: `{{ ansible_facts.user_dir }}/.tmp/bw`

### Example Playbook Bitwarden CLI

```yaml
- name: Include Bitwarden CLI
  ansible.builtin.import_role:
      name: arpanrec.nebula.bws
```

### Testing Bitwarden CLI

```bash
molecule test -s role.bw.default
```
