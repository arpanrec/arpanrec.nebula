# Ansible Role: Go (arpanrec.nebula.go)

Installs the [Go](https://golang.org/) programming language runtime in user space along with a configurable set of global Go tools.

## Features

- User-space installation (no root privileges required)
- Automatic latest-version detection via the Go releases API
- Installs `gopls` (language server), `gosh` (shell), and `lazygit` by default
- Configurable list of additional global Go packages

## Requirements

- Debian-based Linux distribution
- `tar` available on the target host

## Variables

| Variable                | Type   | Required | Default                                                                                                            | Example    | Description                                                                                              |
| ----------------------- | ------ | -------- | ------------------------------------------------------------------------------------------------------------------ | ---------- | -------------------------------------------------------------------------------------------------------- |
| `go_rv_install_path`    | `str`  | `false`  | `{{ ansible_facts.user_dir }}/.local/share/go`                                                                     | -          | Directory where Go is extracted.                                                                         |
| `go_rv_version`         | `str`  | `false`  | `fetch_latest_version`                                                                                             | `go1.23.2` | Go release version. Set to `fetch_latest_version` to resolve the latest from `golang.org` automatically. |
| `go_rv_tmp_dir`         | `str`  | `false`  | `{{ ansible_facts.user_dir }}/.tmp/go`                                                                             | -          | Temporary directory used during download and extraction.                                                 |
| `go_rv_global_installs` | `list` | `false`  | `["golang.org/x/tools/gopls@latest", "mvdan.cc/sh/v3/cmd/gosh@latest", "github.com/jesseduffield/lazygit@latest"]` | -          | List of Go module paths to install globally via `go install`.                                            |

## Example Playbook

```yaml
- name: Install Go
  hosts: all
  roles:
      - name: arpanrec.nebula.go
```

Pin a specific version and add extra tools:

```yaml
- name: Install Go
  hosts: all
  roles:
      - name: arpanrec.nebula.go
        vars:
            go_rv_version: 'go1.23.2'
            go_rv_global_installs:
                - golang.org/x/tools/gopls@latest
                - github.com/go-delve/delve/cmd/dlv@latest
```

## Testing

```bash
molecule test -s role.go.default
```
