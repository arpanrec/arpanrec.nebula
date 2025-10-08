# Ansible Role: Bitwarden Desktop (arpanrec.nebula.bitwarden_desktop)

This role installs the Bitwarden Desktop application as an AppImage, providing a secure password manager with desktop integration. The role automatically detects the latest version and sets up desktop shortcuts.

**Features:**

- Automatic latest version detection from GitHub releases
- AppImage installation for easy deployment and updates
- Desktop integration with .desktop file creation
- User-space installation (no root privileges required)
- Configurable installation paths
- XDG icon support for desktop environments

Install bitwarden AppImage [Bitwarden Desktop](https://github.com/bitwarden/clients)

## Variables

| Variable                             | Type  | Required | Default                                                                      | Example              | Description                                                                                                                                                                                                |
| ------------------------------------ | ----- | -------- | ---------------------------------------------------------------------------- | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bitwarden_desktop_rv_version`       | `str` | `false`  | `fetch_latest_version`                                                       | `desktop-v2024.10.1` | [Bitwarden Desktop Release](https://github.com/bitwarden/clients/releases?q=Desktop&expanded=true) version like `desktop_*`. Dynamically get the latest version if not provided or `fetch_latest_version`. |
| `bitwarden_desktop_rv_install_path`  | `str` | `false`  | `{{ pv_ua_user_share_dir }}/bitwarden-desktop`                               | -                    | Install directory                                                                                                                                                                                          |
| `bitwarden_desktop_rv_xdg_icon_path` | `str` | `false`  | `{{ pv_ua_user_share_dir }}/applications/bitwarden-desktop-userapps.desktop` | -                    | `.desktop` icon file location                                                                                                                                                                              |

## Example Playbook Bitwarden Desktop

```yaml
- name: Include bitwarden_desktop
  ansible.builtin.import_role:
      name: arpanrec.nebula.bitwarden_desktop
```

## Testing Bitwarden Desktop

```bash
molecule test -s role.bitwarden_desktop.default
```
