# Ansible Role: Postman (arpanrec.nebula.postman)

This role installs Postman API development platform for testing, documenting, and collaborating on APIs. It provides desktop integration and user-space installation for development teams.

**Features:**

- Postman installation with desktop integration
- User-space installation (no root privileges required)
- Desktop shortcut and icon configuration
- Configurable installation and cache directories
- Support for API testing, documentation, and collaboration workflows

Install [postman](https://www.postman.com/)

## Variables

| Variable | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| `postman_rv_install_path` | `str` | `false` | `{{ ansible_facts.user_dir }}/.local/share/Postman` | Postman install path. |
| `postman_rv_xdg_icon_path` | `str` | `false` | `{{ ansible_facts.user_dir }}/.local/share/applications/postman-userapps.desktop` | Desktop icon path. |
| `postman_rv_user_tmp_dir` | `str` | `false` | `{{ ansible_facts.user_dir }}/.tmp/postman_app` | Install cache and temporary directory. |

### Example Playbook postman

```yaml
- name: Include postman
  ansible.builtin.import_role:
      name: arpanrec.nebula.postman
```

### Testing postman

```bash
molecule test -s role.postman.default
```
