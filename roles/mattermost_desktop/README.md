# Ansible Role: Mattermost Desktop (arpanrec.nebula.mattermost_desktop)

This role installs Mattermost Desktop application for team collaboration and communication. It provides a dedicated desktop client for Mattermost servers with notification support and desktop integration.

**Features:**

- Mattermost Desktop installation with latest version detection from GitHub
- Desktop integration with icons and application shortcuts
- User-space installation (no root privileges required)
- Support for multiple Mattermost server connections
- Native desktop notifications and system tray integration
- Configurable installation and cache directories

Install [Mattermost Desktop](https://github.com/mattermost/desktop/releases)

## Variables

| Variable                              | Type  | Required | Default                                                                                           | Example  | Description                                                                             |
| ------------------------------------- | ----- | -------- | ------------------------------------------------------------------------------------------------- | -------- | --------------------------------------------------------------------------------------- |
| `pv_ua_mm_release_version`            | `str` | `false`  | [Latest Github Release](https://api.github.com/repos/mattermost/desktop/releases/latest).tag_name | `v5.1.0` | Release Version of [Mattermost Desktop](https://github.com/mattermost/desktop/releases) |
| `mattermost_desktop_rv_user_tmp_dir`  | `str` | `false`  | `{{ ansible_facts.user_dir }}/.tmp/mattermost_desktop`                                            | -        | Install cache directory                                                                 |
| `mattermost_desktop_rv_install_path`  | `str` | `false`  | `{{ ansible_facts.user_dir }}/.local/share/mattermost-desktop`                                    | -        | Install directory                                                                       |
| `mattermost_desktop_rv_xdg_icon_path` | `str` | `false`  | `{{ ansible_facts.user_dir }}/.local/share/applications/mattermost-desktop-userapps.desktop`      | -        | Linux desktop icon path.                                                                |

## Example Playbook Mattermost Desktop

```yaml
- name: Include bitwarden_desktop
  ansible.builtin.import_role:
      name: arpanrec.nebula.mattermost_desktop
```

## Testing Mattermost Desktop

```bash
molecule test -s role.mattermost_desktop.default
```
