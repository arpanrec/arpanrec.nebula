# Ansible Role: Postman (arpanrec.nebula.postman)

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
