# Ansible Role: Telegram Desktop (arpanrec.nebula.telegram_desktop)

This role installs Telegram Desktop messaging application with desktop integration. It provides secure messaging, file sharing, and communication features with automatic version detection.

**Features:**

- Telegram Desktop installation with latest version detection from GitHub
- Desktop integration with icons and application shortcuts
- User-space installation (no root privileges required)
- Configurable installation and working directories
- Secure messaging and file sharing capabilities
- Support for group chats, channels, and bot integration

Install [Telegram Desktop](https://desktop.telegram.org/)

## Variables

| Variable | Type | Required | Default | Example | Description |
|----------|------|----------|---------|---------|-------------|
| `telegram_desktop_rv_install_path` | `str` | `false` | `{{ ansible_facts.user_dir }}/.local/share/telegram_desktop_userapp` | - | Telegram install path. |
| `telegram_desktop_rv_xdg_icon_path` | `str` | `false` | `{{ ansible_facts.user_dir }}/.local/share/applications/telegram_desktop_userapps.desktop` | - | Telegram icon path. |
| `telegram_desktop_rv_user_tmp_dir` | `str` | `false` | `{{ ansible_facts.user_dir }}/.tmp/telegram_desktop_userapp` | - | Telegram install cache and temporary directory. |
| `telegram_desktop_rv_version_number` | `str` | `false` | - | `4.4.1` | Version number. When absent, reads the latest version from [GitHub](https://api.github.com/repos/telegramdesktop/tdesktop/releases/latest). |
| `telegram_desktop_rv_work_directory` | `str` | `false` | `{{ ansible_facts.user_dir }}/.local/share/TelegramDesktop` | - | Application work directory. |

## Example Playbook Telegram Desktop

```yaml
- name: Include Telegram Desktop
  ansible.builtin.import_role:
      name: arpanrec.nebula.telegram_desktop
```

## Testing Telegram Desktop

```bash
molecule test -s role.telegram_desktop.default
```
