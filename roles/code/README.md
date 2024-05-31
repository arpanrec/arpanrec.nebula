# Ansible Role: Microsoft Visual Studio Code (arpanrec.nebula.code)

Install vscode, and extensions Also creates a soft link to the `code` executable in `{{ code_rv_bin_dir }}`

## Variables

```yaml
options:
    code_rv_tmp_dir:
        description: Tarball download location.
        required: false
        type: str
        default: "{{ ansible_facts.user_dir }}/.tmp/code"
    code_rv_bin_dir:
        description:
            - Code executable directory,.
            - This path expected to be in ${PATH}.
        required: false
        type: str
        default: "{{ ansible_facts.user_dir }}/.local/bin"
    code_rv_install_path:
        description: Install Path.
        required: false
        type: str
        default: "{{ ansible_facts.user_dir }}/.local/share/vscode"
    code_rv_xdg_icon_dir:
        description: XDG icon directory.
        required: false
        type: str
        default: "{{ ansible_facts.user_dir }}/.local/share/applications"
    code_rv_version:
        description: Version of [Microsoft Visual Studio Code](https://code.visualstudio.com/updates).
        required: false
        type: str
        default: Dynamically find the [latest tag_name](https://api.github.com/repos/microsoft/vscode/releases/latest), like `1.64.2`.
    code_rv_ext_to_be_installed:
        description: List of VSCode extension to be installed.
        required: false
        type: list[str]
        default:
            - angular.ng-template
            - bradlc.vscode-tailwindcss
            - davidanson.vscode-markdownlint
            - dbaeumer.vscode-eslint
            - dhruv.maven-dependency-explorer
            - dsznajder.es7-react-js-snippets
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
            - gitlab.gitlab-workflow
            - golang.go
            - hashicorp.terraform
            - johnpapa.angular2
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
            - ms-vscode.azure-repos
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
            - sumneko.lua
            - timonwong.shellcheck
            - visualstudioexptteam.intellicode-api-usage-examples
            - visualstudioexptteam.vscodeintellicode
            - visualstudioexptteam.vscodeintellicode-completions
            - wholroyd.jinja
            - yzhang.markdown-all-in-one
```

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
