# Ansible Role: Pulumi (arpanrec.nebula.pulumi)

## Pulumi

Install [Pulumi](https://github.com/pulumi/pulumi) in user space.

## Variable

| Variable | Type | Required | Default | Example | Description |
|----------|------|----------|---------|---------|-------------|
| `pulumi_rv_install_path` | `str` | `false` | `{{ ansible_facts.user_dir }}/.pulumi/bin` | - | Install path for pulumi. |
| `pulumi_rv_version` | `str` | `false` | `fetch_latest_version` | `v3.116.0` | Release version. If set to `fetch_latest_version`, it will fetch latest release from [Github releases](https://api.github.com/repos/pulumi/pulumi/releases/latest). |
| `pulumi_rv_tmp_install_cache_dir` | `str` | `false` | `{{ ansible_facts.user_dir }}/.tmp/pulumi` | - | Cache install directory. |

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
