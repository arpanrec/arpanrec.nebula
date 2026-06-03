# Ansible Role: User Add (arpanrec.nebula.user_add)

Creates a system user with configurable UID/GID, primary and secondary groups, SSH public key authentication, sudo privileges, and password-less command grants.

## Features

- User and primary group creation with optional UID/GID assignment
- Secondary group membership
- SSH `authorized_keys` management for remote access
- Sudo entry with optional password-less command list
- Configurable login shell and home directory

## Requirements

- Debian-based Linux distribution
- Root or sudo privileges on the target host

## Variables

| Variable                                         | Type        | Required | Default                      | Description                                                                                  |
| ------------------------------------------------ | ----------- | -------- | ---------------------------- | -------------------------------------------------------------------------------------------- |
| `user_add_rv_username`                           | `str`       | **true** | -                            | Login name for the new user.                                                                 |
| `user_add_rv_user_primary_group`                 | `str`       | `false`  | `{{ user_add_rv_username }}` | Name of the user's primary group.                                                            |
| `user_add_rv_user_primary_gid`                   | `int`       | `false`  | -                            | Numeric GID for the primary group. Omitted if not set.                                       |
| `user_add_rv_uid`                                | `int`       | `false`  | -                            | Numeric UID for the user. Omitted if not set (system assigns next available).                |
| `user_add_rv_password`                           | `str`       | `false`  | -                            | Plaintext password for the user (hashed before setting). Leave unset for no password.        |
| `user_add_rv_user_extra_groups`                  | `list[str]` | `false`  | -                            | Additional groups to add the user to (e.g. `["docker", "sudo"]`).                            |
| `user_add_rv_ssh_access_public_key_content_list` | `list[str]` | `false`  | -                            | List of SSH public key strings to add to `~/.ssh/authorized_keys`.                           |
| `user_add_rv_user_nopasswd_commands`             | `list[str]` | `false`  | -                            | Commands the user may run without a password (written to `/etc/sudoers.d/`).                 |
| `user_add_rv_user_default_shell`                 | `str`       | `false`  | `/bin/bash`                  | Login shell path.                                                                            |
| `user_add_rv_user_home_dir`                      | `str`       | `false`  | -                            | Explicit home directory path. Defaults to system convention (`/home/<username>`) if not set. |

## Example Playbook

Create a basic user with SSH access:

```yaml
- name: Add application user
  hosts: all
  roles:
      - name: arpanrec.nebula.user_add
        vars:
            user_add_rv_username: 'deploy'
            user_add_rv_ssh_access_public_key_content_list:
                - 'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAA...'
```

Create a user with sudo and password-less service restart:

```yaml
- name: Add admin user
  hosts: all
  roles:
      - name: arpanrec.nebula.user_add
        vars:
            user_add_rv_username: 'ops'
            user_add_rv_user_extra_groups:
                - sudo
            user_add_rv_user_nopasswd_commands:
                - /usr/bin/systemctl restart myapp
                - /usr/bin/systemctl status myapp
            user_add_rv_ssh_access_public_key_content_list:
                - 'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAA...'
            user_add_rv_user_default_shell: /bin/zsh
```

## Testing

Prerequisite: `docker`, `python3-venv`

```bash
molecule test -s role.user_add.default
```
