# Ansible Role Linux Patching (arpanrec.nebula.linux_patching)

Install all latest packages in Debian based systems.
Also Install basic utility tools for server.
Set timezone, locale, and loopback ip in server

## Role Variables

- `linux_patching_rv_upgrade_existing_packages`

  - Description: If set to `true` Upgrade the existing packages in OS.
  - Required: `false`
  - Default: `true`
  - Type: `bool`

- `linux_patching_rv_packages`

  - Description: Install the packages in the distributions.
  - Required: `false`
  - Default:
    - zip
    - unzip
    - tar
    - wget
    - curl
    - ca-certificates
    - sudo
    - systemd
    - gnupg2
    - apt-transport-https
    - locales
    - systemd-timesyncd
    - network-manager
    - gnupg2
    - gnupg
    - pigz
    - cron
    - acl
    - ufw
    - bzip2
    - procps
    - xz-utils
    - apt-utils
    - lsb-release
    - software-properties-common
    - python3

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

- `linux_patching_rv_managed_packages`

  - Description: Install the managed packages in the distributions.
  - Required: `false`
  - Default: List of packages

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
  become: true
  become_method: su
  any_errors_fatal: true
  ansible.builtin.import_role:
      name: arpanrec.nebula.linux_patching
```

## Testing

```bash
molecule test -s role.linux_patching.default
```
