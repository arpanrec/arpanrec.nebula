# Ansible Role Linux Patching (arpanrec.nebula.linux_patching)

Install all latest packages in Debian based systems.
Also Install basic utility tools for server.
Set timezone, locale, and loopback ip in server

## Role Variables

| Variable | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| `linux_patching_rv_packages` | `list[str]` | `false` | See default list below | Install the packages in the distributions. |
| `linux_patching_rv_devel_packages` | `list[str]` | `false` | See default list below | Install the development packages in the distributions. |
| `linux_patching_rv_install_devel_packages` | `bool` | `false` | `true` | Install the development packages in the distributions. |
| `linux_patching_rv_extra_packages` | `list[str]` | `false` | - | Install extra required the packages. |
| `linux_patching_rv_timezone` | `str` | `false` | `Asia/Kolkata` | Set the ZoneTime info in server. |
| `linux_patching_rv_hostname` | `str` | `false` | `localhost` or `{{ ansible_facts['hostname'] }}` | Cluster / Public Host name. (Doesn't work with docker) |
| `linux_patching_rv_domain_name` | `str` | `false` | `{{ ansible_facts['domain'] }}` | Domain Name |
| `linux_patching_rv_root_ca_pem_content` | `str` | `false` | - | Organization Root CA certificate. |
| `linux_patching_rv_ssh_port` | `int` | `false` | `22` | Default SSH Port |

### Default Packages (`linux_patching_rv_packages`)

```yaml
linux_patching_rv_packages:
  - ca-certificates
  - sudo
  - systemd
  - apt-transport-https
  - locales
  - systemd-timesyncd
  - network-manager
  - gnupg2
  - gnupg
  - acl
  - ufw
  - procps
  - apt-utils
  - lsb-release
  - software-properties-common
  - python3
  - openssl
```

### Default Development Packages (`linux_patching_rv_devel_packages`)

```yaml
linux_patching_rv_devel_packages:
  - net-tools
  - telnet
  - vim
  - git
  - jq
  - zsh
  - htop
  - tmux
  - tree
  - neovim
  - python3-neovim
  - luarocks
  - build-essential
  - ninja-build
  - gettext
  - cmake
  - make
  - openssh-client
  - rsync
  - ntfs-3g
  - exfat-fuse
  - python3-pip
  - python3-venv
  - python3-dev
  - python3-pynvim
  - fd-find
  - ripgrep
  - rclone
  - zip
  - unzip
  - tar
  - wget
  - curl
  - pigz
  - xz-utils
  - gzip
  - bzip2
```

## Example Playbook

```yaml
---
- name: Patch Debian System
  ansible.builtin.import_role:
      name: arpanrec.nebula.linux_patching
```

## Testing

```bash
molecule test -s role.linux_patching.default
```
