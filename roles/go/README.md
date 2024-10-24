# Ansible Role: GoLang (arpanrec.nebula.go)

## Go Language

Install Go Language in user space

## Variables Go Language

```yaml
options:
    go_rv_install_path:
        description: Install path for Go.
        required: false
        type: str
        default: "{{ ansible_facts.user_dir }}/.local/share/go"
    go_rv_version:
        description:
            - Exact release version of go language.
            - Example Format `go1.23.2`.
            - If set to `fetch_latest_version`, it will fetch the latest version from [golang](https://golang.org/VERSION?m=text).
        required: false.
        type: str.
        default: "fetch_latest_version".
    go_rv_tmp_dir:
        description: Temporary cache directory for install.
        required: false
        type: str
        default: "{{ ansible_facts.user_dir }}/.tmp/go"
```

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
