# Ansible Role: Node.js (arpanrec.nebula.nodejs)

Installs the [Node.js](https://nodejs.org/) runtime in user space along with a configurable set of global npm packages.

## Features

- User-space installation (no root privileges required)
- Automatic latest-version detection via the Node.js GitHub releases API
- Default global packages: `@bitwarden/cli`, `neovim`, `semver`, `corepack`
- Configurable list of additional global npm packages

## Requirements

- Debian-based Linux distribution
- `tar` available on the target host

## Variables

| Variable                          | Type   | Required | Default                                              | Example   | Description                                                                                             |
| --------------------------------- | ------ | -------- | ---------------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------- |
| `nodejs_rv_install_path`          | `str`  | `false`  | `{{ ansible_facts.user_dir }}/.local/share/node`     | -         | Directory where Node.js is extracted.                                                                   |
| `nodejs_rv_version`               | `str`  | `false`  | `fetch_latest_version`                               | `v22.9.0` | Node.js release version. Set to `fetch_latest_version` to resolve the latest from GitHub automatically. |
| `nodejs_rv_tmp_install_cache_dir` | `str`  | `false`  | `{{ ansible_facts.user_dir }}/.tmp/nodejs`           | -         | Temporary directory used during download and extraction.                                                |
| `nodejs_rv_global_packages`       | `list` | `false`  | `["@bitwarden/cli", "neovim", "semver", "corepack"]` | -         | List of npm package names to install globally via `npm install -g`.                                     |

## Example Playbook

```yaml
- name: Install Node.js
  hosts: all
  roles:
      - name: arpanrec.nebula.nodejs
```

Pin a version and customize global packages:

```yaml
- name: Install Node.js
  hosts: all
  roles:
      - name: arpanrec.nebula.nodejs
        vars:
            nodejs_rv_version: 'v22.9.0'
            nodejs_rv_global_packages:
                - '@bitwarden/cli'
                - neovim
                - typescript
                - tsx
```

## Testing

```bash
molecule test -s role.nodejs.default
```
