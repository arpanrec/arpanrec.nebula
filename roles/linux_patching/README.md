# Ansible Role Linux Patching (arpanrec.nebula.linux_patching)

Install all latest packages in Debian based systems.
Also Install basic utility tools for server.
Set timezone, locale, and loopback ip in server

## Role Variables

- `linux_patching_rv_packages`

  - Description: Install the packages in the distributions.
  - Required: `false`
  - Default:
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

- Type: `list[str]`

- `linux_patching_rv_devel_packages`
  
  - Description: Install the development packages in the distributions.
  - Required: `false`
  - Type: `list[str]`
  - Default:
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

- `linux_patching_rv_install_devel_packages`
  - Description: Install the development packages in the distributions.
  - Required: `false`
  - Type: `bool`
  - Default: `true`

- `linux_patching_rv_extra_packages`

  - Description: Install extra required the packages.
  - Required: `false`
  - Type: `list[str]`

- `linux_patching_rv_timezone`

  - Description: Set the ZoneTime info in server.
  - Required: `false`
  - Default: `Asia/Kolkata`
  - Type: `str`

- `linux_patching_rv_hostname`

  - Description: Cluster / Public Host name. (Doesn't work with docker)
  - Required: `false`
  - Type: `str`
  - Default: `localhost` or `{{ ansible_facts['hostname'] }}`

- `linux_patching_rv_domain_name`
  - Description: Domain Name
  - Required: `false`
  - Type: `str`
  - Default: `{{ ansible_facts['domain'] }}`

- `linux_patching_rv_root_ca_pem_content`

  - Description: Organization Root CA certificate.
  - Required: `false`
  - Type: `str`

- `linux_patching_rv_ssh_port`

  - Description: Default SSH Port
  - Required: `false`
  - Type: `int`
  - Default: `22`

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
