# Ansible Role: Gitleaks (arpanrec.nebula.gitleaks)

Installs [Gitleaks](https://github.com/gitleaks/gitleaks) in user space. Gitleaks is a secret-detection tool that scans git repositories, files, and stdin for leaked passwords, API keys, tokens, and other sensitive values using a regex-based detection engine.

## Features

- User-space installation (no root privileges required)
- Automatic latest-version detection via the GitHub Releases API
- Configurable installation and cache directories
- Suitable for pre-commit hooks, CI/CD pipelines, and ad-hoc scans

## Requirements

- Debian-based Linux distribution
- `tar` available on the target host

## Variables

| Variable                          | Type  | Required | Default                                      | Example  | Description                                                                                                         |
| --------------------------------- | ----- | -------- | -------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------- |
| `gitleaks_rv_executable_bin_path` | `str` | `false`  | `{{ ansible_facts.user_dir }}/.local/bin`    | -        | Directory where the `gitleaks` binary is placed.                                                                    |
| `gitleaks_rv_version`             | `str` | `false`  | `fetch_latest_version`                       | `8.28.0` | Version to install. Set to `fetch_latest_version` to resolve the latest from the GitHub Releases API automatically. |
| `gitleaks_rv_tmp_download_dir`    | `str` | `false`  | `{{ ansible_facts.user_dir }}/.tmp/gitleaks` | -        | Temporary directory used during download and extraction.                                                            |

## Example Playbook

```yaml
- name: Install Gitleaks
  hosts: all
  roles:
      - name: arpanrec.nebula.gitleaks
```

Pin a specific version:

```yaml
- name: Install Gitleaks
  hosts: all
  roles:
      - name: arpanrec.nebula.gitleaks
        vars:
            gitleaks_rv_version: '8.28.0'
```

## Testing

```bash
molecule test -s role.gitleaks.default
```
