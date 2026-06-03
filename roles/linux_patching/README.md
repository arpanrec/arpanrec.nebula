# Ansible Role: Linux Patching (arpanrec.nebula.linux_patching)

Performs system package updates and baseline configuration on Debian-based systems. Installs essential system and development packages, configures timezone/locale/hostname, manages UFW firewall rules, and optionally installs a custom root CA certificate.

## Features

- Full apt package upgrade and configurable package installation
- Separate base and development package lists, independently toggleable
- Timezone, locale, and hostname/domain configuration
- UFW firewall with SSH port allowance
- Custom root CA certificate installation for organization PKI
- SSH port configuration for `ufw` rules

## Requirements

- Debian-based Linux distribution (Debian, Ubuntu)
- Root or sudo privileges on the target host

## Variables

| Variable                                   | Type        | Required | Default                        | Description                                                                                          |
| ------------------------------------------ | ----------- | -------- | ------------------------------ | ---------------------------------------------------------------------------------------------------- |
| `linux_patching_rv_packages`               | `list[str]` | `false`  | See below                      | Base system packages to install.                                                                     |
| `linux_patching_rv_devel_packages`         | `list[str]` | `false`  | See below                      | Development packages to install. Skipped when `linux_patching_rv_install_devel_packages` is `false`. |
| `linux_patching_rv_install_devel_packages` | `bool`      | `false`  | `true`                         | Set to `false` to skip development package installation.                                             |
| `linux_patching_rv_extra_packages`         | `list[str]` | `false`  | -                              | Additional packages to install alongside the base list.                                              |
| `linux_patching_rv_timezone`               | `str`       | `false`  | `Asia/Kolkata`                 | System timezone (e.g. `UTC`, `America/New_York`).                                                    |
| `linux_patching_rv_hostname`               | `str`       | `false`  | `{{ ansible_facts.hostname }}` | Hostname to set on the system. Has no effect inside Docker containers.                               |
| `linux_patching_rv_domain_name`            | `str`       | `false`  | `{{ ansible_facts.domain }}`   | Domain name appended to the hostname for FQDN resolution.                                            |
| `linux_patching_rv_root_ca_pem_content`    | `str`       | `false`  | -                              | PEM content of a custom root CA certificate to trust system-wide.                                    |
| `linux_patching_rv_ssh_port`               | `int`       | `false`  | `22`                           | SSH port opened in the UFW firewall.                                                                 |

### Default Base Packages (`linux_patching_rv_packages`)

```
ca-certificates, sudo, systemd, apt-transport-https, locales,
systemd-timesyncd, network-manager, gnupg2, gnupg, acl, ufw,
procps, apt-utils, lsb-release, python3, openssl,
util-linux-extra, nftables, libatomic1
```

### Default Development Packages (`linux_patching_rv_devel_packages`)

```
net-tools, telnet, vim, git, git-lfs, jq, zsh, htop, tmux, tree,
neovim, python3-neovim, luarocks, build-essential, ninja-build,
gettext, cmake, make, openssh-client, rsync, ntfs-3g, exfat-fuse,
python3-pip, python3-venv, python3-dev, python3-pynvim, fd-find,
ripgrep, rclone, zip, unzip, tar, wget, curl, pigz, xz-utils,
gzip, bzip2, autoconf, automake, gcc, g++, clang,
libglib2.0-dev, libssl-dev, libffi-dev, zlib1g-dev
```

## Example Playbook

Minimal run with defaults:

```yaml
- name: Patch Debian system
  hosts: all
  roles:
      - name: arpanrec.nebula.linux_patching
```

Server-only baseline (skip dev tools, set timezone and hostname):

```yaml
- name: Patch Debian system
  hosts: all
  roles:
      - name: arpanrec.nebula.linux_patching
        vars:
            linux_patching_rv_install_devel_packages: false
            linux_patching_rv_timezone: 'UTC'
            linux_patching_rv_hostname: 'myserver'
            linux_patching_rv_domain_name: 'example.com'
```

Install a custom root CA certificate:

```yaml
- name: Patch Debian system with custom CA
  hosts: all
  roles:
      - name: arpanrec.nebula.linux_patching
        vars:
            linux_patching_rv_root_ca_pem_content: "{{ lookup('file', 'corp-root-ca.pem') }}"
```

## Testing

```bash
molecule test -s role.linux_patching.default
```
