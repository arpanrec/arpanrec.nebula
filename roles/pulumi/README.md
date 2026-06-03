# Ansible Role: Pulumi (arpanrec.nebula.pulumi)

Installs the [Pulumi](https://www.pulumi.com/) infrastructure-as-code CLI in user space. Pulumi lets you define and manage cloud infrastructure using familiar programming languages (TypeScript, Python, Go, C#, Java, YAML).

## Features

- User-space installation (no root privileges required)
- Automatic latest-version detection via the GitHub Releases API
- Configurable installation and cache directories
- Compatible with AWS, Azure, GCP, Kubernetes, and 150+ cloud providers

## Requirements

- Debian-based Linux distribution
- `tar` available on the target host

## Variables

| Variable                          | Type  | Required | Default                                    | Example    | Description                                                                                                         |
| --------------------------------- | ----- | -------- | ------------------------------------------ | ---------- | ------------------------------------------------------------------------------------------------------------------- |
| `pulumi_rv_install_path`          | `str` | `false`  | `{{ ansible_facts.user_dir }}/.pulumi/bin` | -          | Directory where Pulumi binaries are placed.                                                                         |
| `pulumi_rv_version`               | `str` | `false`  | `fetch_latest_version`                     | `v3.116.0` | Version to install. Set to `fetch_latest_version` to resolve the latest from the GitHub Releases API automatically. |
| `pulumi_rv_tmp_install_cache_dir` | `str` | `false`  | `{{ ansible_facts.user_dir }}/.tmp/pulumi` | -          | Temporary directory used during download and extraction.                                                            |

## Example Playbook

```yaml
- name: Install Pulumi
  hosts: all
  roles:
      - name: arpanrec.nebula.pulumi
```

Pin a specific version:

```yaml
- name: Install Pulumi
  hosts: all
  roles:
      - name: arpanrec.nebula.pulumi
        vars:
            pulumi_rv_version: 'v3.116.0'
            pulumi_rv_install_path: '{{ ansible_facts.user_dir }}/.pulumi/bin'
```

## Testing

```bash
molecule test -s role.pulumi.default
```
