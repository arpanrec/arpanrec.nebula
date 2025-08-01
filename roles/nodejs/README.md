# Ansible Role: NodeJS (arpanrec.nebula.nodejs)

## NodeJS

This role installs Node.js runtime environment in user space along with popular global packages. It automatically configures the environment and installs essential development tools.

**Features:**

- Latest Node.js version installation with automatic detection
- Global package management (npm/yarn/pnpm)
- Essential development tools (Bitwarden CLI, Neovim support, etc.)
- User-space installation (no root privileges required)
- Configurable package list for team consistency

## Variable

| Variable | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| `nodejs_rv_install_path` | `str` | `false` | `{{ ansible_facts.user_dir }}/.local/share/node` | Install path for nodejs. |
| `nodejs_rv_version` | `str` | `false` | `fetch_latest_version` | Release version. If set to `fetch_latest_version`, it will fetch the latest version from [Github](https://github.com/nodejs/node/releases). |
| `nodejs_rv_tmp_install_cache_dir` | `str` | `false` | `{{ ansible_facts.user_dir }}/.tmp/nodejs` | Cache install directory. |
| `nodejs_rv_global_packages` | `list` | `false` | `["@bitwarden/cli", "neovim", "yarn", "pnpm", "semver"]` | List of global packages to install. |

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
