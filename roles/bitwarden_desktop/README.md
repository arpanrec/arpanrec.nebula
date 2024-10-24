# Ansible Role: Bitwarden Desktop (arpanrec.nebula.bitwarden_desktop)

Install bitwarden AppImage [Bitwarden Desktop](https://github.com/bitwarden/clients)

## Variables

- `bitwarden_desktop_rv_version`

  - Description:
    - [Bitwarden Desktop Release](https://github.com/bitwarden/clients/releases?q=Desktop&expanded=true) version like `desktop_*`.
    - Dynamically get the latest version if not provided or `fetch_latest_version`.
  - Type: `str`.
  - Required: `false`.
  - Default: `fetch_latest_version`.
  - Example: `desktop-v2024.10.1`.

- `bitwarden_desktop_rv_install_path`

  - Description: Install directory
  - Default: `{{ pv_ua_user_share_dir }}/bitwarden-desktop`
  - Type: `str`
  - Required: `false`

- `bitwarden_desktop_rv_xdg_icon_path`

  - Description: `.desktop` icon file location
  - Default: `{{ pv_ua_user_share_dir }}/applications/bitwarden-desktop-userapps.desktop`
  - Type: `str`
  - Required: `false`

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
