# Ansible Role User Add (arpanrec.nebula.user_add)

This role creates system users with comprehensive configuration including group membership, SSH access, and sudo privileges. It provides secure user provisioning for development and server environments.

**Features:**

- User account creation with configurable UID/GID
- Primary and secondary group management
- SSH public key authentication setup
- Sudo privileges configuration with granular command control
- Password-less command execution for specific operations
- Home directory and shell configuration
- Secure user provisioning for team environments

Create a user and add it to sudoers.d

## Role Variables

| Variable                                         | Type           | Required | Default                      | Description                                        |
| ------------------------------------------------ | -------------- | -------- | ---------------------------- | -------------------------------------------------- |
| `user_add_rv_user_primary_group`                 | `String`       | `false`  | `{{ user_add_rv_username }}` | Group Name : Primary Group of the user             |
| `user_add_rv_user_primary_gid`                   | `int`          | `false`  | `omit`                       | Group ID : GID for primary group                   |
| `user_add_rv_username`                           | `String`       | `true`   | -                            | Username                                           |
| `user_add_rv_uid`                                | `int`          | `false`  | `omit`                       | User ID : UID                                      |
| `user_add_rv_password`                           | `String`       | `false`  | -                            | Clear text password for the user                   |
| `user_add_rv_user_extra_groups`                  | `List<String>` | `false`  | -                            | Groups : Extra groups for user                     |
| `user_add_rv_ssh_access_public_key_content_list` | `list<str>`    | `false`  | -                            | Public key for remote ssh access                   |
| `user_add_rv_user_nopasswd_commands`             | `List<String>` | `false`  | -                            | Commands user will be able to run without password |
| `user_add_rv_user_default_shell`                 | `str`          | `false`  | `/bin/bash`                  | Default shell for the User                         |
| `user_add_rv_user_home_dir`                      | `str`          | `false`  | -                            | Path to home                                       |

## Example Playbook

```yaml
- name: Add application user
  ansible.builtin.import_role:
      name: arpanrec.nebula.user_add
  vars:
      user_add_rv_username: 'arpan'
      user_add_rv_ssh_access_public_key_content_list: ['ssh-rsa yc2E']
```

## Testing

Prerequisite: `docker`, `python3-venv`

```bash
molecule test -s role.user_add.default
```
