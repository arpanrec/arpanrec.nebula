# Ansible Role: Microsoft Visual Studio Code (arpanrec.nebula.code)

Install vscode, and extensions Also creates a soft link to the `code` executable in `{{ code_rv_bin_dir }}`

## Variables

| Variable | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| `code_rv_tmp_dir` | `str` | `false` | `{{ ansible_facts.user_dir }}/.tmp/code` | Tarball download location. |
| `code_rv_bin_dir` | `str` | `false` | `{{ ansible_facts.user_dir }}/.local/bin` | Code executable directory. This path expected to be in ${PATH}. |
| `code_rv_install_path` | `str` | `false` | `{{ ansible_facts.user_dir }}/.local/share/vscode` | Install Path. |
| `code_rv_xdg_icon_dir` | `str` | `false` | `{{ ansible_facts.user_dir }}/.local/share/applications` | XDG icon directory. |
| `code_rv_version` | `str` | `false` | `fetch_latest_version` | Version of [Microsoft Visual Studio Code](https://code.visualstudio.com/updates). If set to `fetch_latest_version`, it will fetch the latest release from the [api](https://update.code.visualstudio.com/api/releases/stable). Dynamically find the [latest tag_name](https://update.code.visualstudio.com/api/releases/stable), like `1.64.2`. |
| `code_rv_ext_to_be_installed` | `list[str]` | `false` | See default list below | List of VSCode extension to be installed. |

### Default Extensions (`code_rv_ext_to_be_installed`)

```yaml
code_rv_ext_to_be_installed:
      - angular.ng-template
      - bradlc.vscode-tailwindcss
      - davidanson.vscode-markdownlint
      - dbaeumer.vscode-eslint
      - esbenp.prettier-vscode
      - exiasr.hadolint
      - foxundermoon.shell-format
      - github.codespaces
      - github.copilot
      - github.copilot-chat
      - github.github-vscode-theme
      - github.remotehub
      - github.vscode-codeql
      - github.vscode-github-actions
      - github.vscode-pull-request-github
      - golang.go
      - hashicorp.terraform
      - ms-azuretools.vscode-docker
      - ms-python.black-formatter
      - ms-python.debugpy
      - ms-python.isort
      - ms-python.mypy-type-checker
      - ms-python.pylint
      - ms-python.python
      - ms-python.vscode-pylance
      - ms-toolsai.jupyter
      - ms-toolsai.jupyter-keymap
      - ms-toolsai.jupyter-renderers
      - ms-toolsai.vscode-jupyter-cell-tags
      - ms-toolsai.vscode-jupyter-slideshow
      - ms-vscode-remote.remote-containers
      - ms-vscode-remote.remote-ssh
      - ms-vscode-remote.remote-ssh-edit
      - ms-vscode-remote.remote-wsl
      - ms-vscode-remote.vscode-remote-extensionpack
      - ms-vscode.remote-explorer
      - ms-vscode.remote-repositories
      - ms-vscode.remote-server
      - ms-vscode.vscode-speech
      - msjsdiag.vscode-react-native
      - pkief.material-icon-theme
      - redhat.ansible
      - redhat.fabric8-analytics
      - redhat.vscode-xml
      - redhat.vscode-yaml
      - rust-lang.rust-analyzer
      - streetsidesoftware.code-spell-checker
      - timonwong.shellcheck
      - visualstudioexptteam.intellicode-api-usage-examples
      - visualstudioexptteam.vscodeintellicode
      - visualstudioexptteam.vscodeintellicode-completions
      - wholroyd.jinja
      - yzhang.markdown-all-in-one

## Example Playbook Visual Studio Code

```yaml
---
- name: Visual Studio Code
  roles:
      - name: arpanrec.nebula.code
```

## Testing Visual Studio Code

```bash
molecule test -s role.code.default
```
