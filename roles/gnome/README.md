# Ansible Role: Gnome Desktop (arpanrec.nebula.gnome)

Install Gnome Extensions and setup

## Variables

| Variable | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| `gnome_rv_extension_list` | `list[dict]` | `false` | See default list below | List of Extensions with `name` and `id` properties |
| `gnome_rv_user_share_dir` | `str` | `false` | `{{ ansible_facts.user_dir }}/.local/share` | User share directory. Extensions will be install in `{{ gnome_rv_user_share_dir }}/gnome-shell/extensions/<uuid>` |
| `gnome_rv_user_cache_tmp_dir` | `str` | `false` | `{{ ansible_facts.user_dir }}/.tmp/gnome_ansible` | Install cache and temporary directory. |

### Default Extensions (`gnome_rv_extension_list`)

```yaml
gnome_rv_extension_list:
  - name: "user-themes"
    id: 19
  - name: "AppIndicator and KStatusNotifierItem Support"
    id: 615
  - name: "workspace-indicator"
    id: 21
  - name: "applications-menu"
    id: 6
  - name: "vitals"
    id: 1460
```

## Example Playbook Gnome

```yaml
- name: Include Gnome
  ansible.builtin.import_role:
      name: arpanrec.nebula.gnome
```

## Testing Gnome

```bash
molecule test -s role.gnome.default
```
