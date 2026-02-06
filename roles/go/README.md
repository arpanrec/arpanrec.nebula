# Ansible Role: GoLang (arpanrec.nebula.go)

## Go Language

This role installs the Go programming language runtime and essential development tools in user space. It sets up a complete Go development environment with popular tools and utilities.

**Features:**

- Go language runtime installation with the latest version detection
- Essential development tools (gopls, gosh, lazygit)
- User-space installation (no root privileges required)
- Automatic environment configuration
- Global package management for consistent tooling across teams

## Variables Go Language

| Variable                | Type   | Required | Default                                                                                                            | Description                                                                                                                                                                           |
| ----------------------- | ------ | -------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `go_rv_install_path`    | `str`  | `false`  | `{{ ansible_facts.user_dir }}/.local/share/go`                                                                     | Install path for Go.                                                                                                                                                                  |
| `go_rv_version`         | `str`  | `false`  | `fetch_latest_version`                                                                                             | Exact release version of go language. Example Format `go1.23.2`. If set to `fetch_latest_version`, it will fetch the latest version from [golang](https://golang.org/VERSION?m=text). |
| `go_rv_tmp_dir`         | `str`  | `false`  | `{{ ansible_facts.user_dir }}/.tmp/go`                                                                             | Temporary cache directory for install.                                                                                                                                                |
| `go_rv_global_installs` | `list` | `false`  | `["golang.org/x/tools/gopls@latest", "mvdan.cc/sh/v3/cmd/gosh@latest", "github.com/jesseduffield/lazygit@latest"]` | List of global packages to install.                                                                                                                                                   |

## Example Playbook Go Language

```yaml
---
- name: Golang
  hosts: all
  roles:
      - name: arpanrec.nebula.go
```

## Testing Go Language

```bash
molecule test -s role.go.default
```
