# Ansible Role: Hadolint (arpanrec.nebula.hadolint)

Installs [Hadolint](https://github.com/hadolint/hadolint) in user space. Hadolint is a Dockerfile linter that parses Dockerfiles into an AST and validates them against best-practice rules. It integrates [ShellCheck](https://www.shellcheck.net/) to lint shell scripts inside `RUN` instructions.

## Features

- User-space installation (no root privileges required)
- Automatic latest-version detection via the GitHub Releases API
- Configurable installation and cache directories
- Suitable for CI/CD pipelines and pre-commit hooks

## Requirements

- Debian-based Linux distribution

## Variables

| Variable                            | Type  | Required | Default                                            | Example   | Description                                                                                                         |
| ----------------------------------- | ----- | -------- | -------------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------- |
| `hadolint_rv_executable_bin_path`   | `str` | `false`  | `{{ ansible_facts.user_dir }}/.local/bin/hadolint` | -         | Full path (including filename) where the `hadolint` binary is placed.                                               |
| `hadolint_rv_version`               | `str` | `false`  | `fetch_latest_version`                             | `v2.13.1` | Version to install. Set to `fetch_latest_version` to resolve the latest from the GitHub Releases API automatically. |
| `hadolint_rv_tmp_install_cache_dir` | `str` | `false`  | `{{ ansible_facts.user_dir }}/.tmp/hadolint`       | -         | Temporary directory used during download.                                                                           |

## Example Playbook

```yaml
- name: Install Hadolint
  hosts: all
  roles:
      - name: arpanrec.nebula.hadolint
```

Pin a specific version:

```yaml
- name: Install Hadolint
  hosts: all
  roles:
      - name: arpanrec.nebula.hadolint
        vars:
            hadolint_rv_version: 'v2.13.1'
```

## Testing

```bash
molecule test -s role.hadolint.default
```
