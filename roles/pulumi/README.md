# Ansible Role: Pulumi (arpanrec.nebula.pulumi)

## Pulumi

Install [Pulumi](https://github.com/pulumi/pulumi) in user space.

## Variable

- `pulumi_rv_install_path`

  - Description: Install path for pulumi.
  - Default: `"{{ ansible_facts.user_dir }}/.pulumi/bin"`
  - Required: `false`
  - Type: `str`

- `pulumi_rv_version`

  - Description:
    - Release version.
    - Get latest release from [Github releases](https://api.github.com/repos/pulumi/pulumi/releases/latest)
    - Example `v3.116.0`
  - Required: `false`
  - Type: `str`

- `pulumi_rv_tmp_install_cache_dir`

  - Description: Cache install directory.
  - Default: `"{{ ansible_facts.user_dir }}/.tmp/pulumi"`
  - Required: `false`
  - Type: `str`

### Example Playbook Pulumi

```yaml
- name: Include Pulumi
  ansible.builtin.import_role:
      name: arpanrec.nebula.pulumi
```

### Testing Pulumi

```bash
molecule test -s role.pulumi.default
```
