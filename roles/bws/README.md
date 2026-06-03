# Ansible Role: Bitwarden Secrets Manager SDK (arpanrec.nebula.bws)

Installs the [Bitwarden Secrets Manager SDK CLI](https://bitwarden.com/help/secrets-manager-sdk/) (`bws`) in user space. The `bws` CLI enables automated secrets retrieval from Bitwarden Secrets Manager for CI/CD pipelines and server automation.

## Features

- User-space installation (no root privileges required)
- Automatic latest-version detection via the GitHub Releases API
- Configurable installation and cache directories
- Works alongside the `bitwarden` lookup plugin in this collection

## Requirements

- Debian-based Linux distribution
- A Bitwarden Secrets Manager account and machine account access token for runtime use

## Variables

| Variable              | Type  | Required | Default                                   | Example      | Description                                                                                                             |
| --------------------- | ----- | -------- | ----------------------------------------- | ------------ | ----------------------------------------------------------------------------------------------------------------------- |
| `bws_sdk_version_tag` | `str` | `false`  | `fetch_latest_version`                    | `bws-v1.0.0` | Release tag to install. Set to `fetch_latest_version` to resolve the latest from the GitHub Releases API automatically. |
| `bws_sdk_bin_dir`     | `str` | `false`  | `{{ ansible_facts.user_dir }}/.local/bin` | -            | Directory where the `bws` binary is placed.                                                                             |
| `bws_sdk_tmp_dir`     | `str` | `false`  | `{{ ansible_facts.user_dir }}/.tmp/bw`    | -            | Temporary directory used during download and extraction.                                                                |

## Example Playbook

```yaml
- name: Install Bitwarden Secrets Manager CLI
  hosts: all
  roles:
      - name: arpanrec.nebula.bws
```

Pin a specific release:

```yaml
- name: Install Bitwarden Secrets Manager CLI
  hosts: all
  roles:
      - name: arpanrec.nebula.bws
        vars:
            bws_sdk_version_tag: 'bws-v1.0.0'
```

## Testing

```bash
molecule test -s role.bw.default
```
