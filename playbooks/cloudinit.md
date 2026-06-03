# Playbook: Cloud Init (cloudinit.yml)

Bootstraps a fresh cloud instance: creates a non-root user, hardens SSH, configures the system baseline, and optionally installs Docker. Designed to run once immediately after instance creation (e.g., via cloud-init userdata or a post-provision hook).

## Target Host Group

```
cloudinit
```

Define this group in your Ansible inventory pointing at the newly provisioned instance.

## What It Does

1. Applies system baseline — [linux_patching](../roles/linux_patching/README.md)
2. Creates the provisioning user — [user_add](../roles/user_add/README.md)
3. Hardens the SSH daemon and deploys Fail2Ban — [ssh_hardening](../roles/ssh_hardening/README.md)
4. _(Optional)_ Installs Docker via `geerlingguy.docker`

## Extra Variables

| Variable                        | Required | Description                                                                        |
| ------------------------------- | -------- | ---------------------------------------------------------------------------------- |
| `pv_cloud_init_group`           | `false`  | Primary group name for the provisioned user.                                       |
| `pv_cloud_init_user`            | `false`  | Username for the provisioned user.                                                 |
| `pv_cloud_init_authorized_keys` | `false`  | List of SSH public key strings granted access to the provisioned user.             |
| `pv_cloud_init_is_dev_machine`  | `false`  | When `true`, installs development packages via `linux_patching`. Default: `false`. |
| `pv_cloud_init_hostname`        | `false`  | Hostname to configure on the instance.                                             |
| `pv_cloud_init_domain`          | `false`  | Domain name to configure on the instance.                                          |
| `pv_cloud_init_install_docker`  | `false`  | When `true`, installs Docker using `geerlingguy.docker`. Default: `false`.         |

## Usage

Basic bootstrap (system patching and user creation only):

```bash
ansible-playbook playbooks/cloudinit.yml -i inventory.yml \
  --extra-vars "pv_cloud_init_user=ops pv_cloud_init_group=ops"
```

Full bootstrap with SSH keys, hostname, and Docker:

```bash
ansible-playbook playbooks/cloudinit.yml -i inventory.yml \
  --extra-vars '{
    "pv_cloud_init_user": "ops",
    "pv_cloud_init_group": "ops",
    "pv_cloud_init_hostname": "app-server-01",
    "pv_cloud_init_domain": "example.com",
    "pv_cloud_init_install_docker": true,
    "pv_cloud_init_authorized_keys": ["ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAA..."]
  }'
```

Using a vars file:

```yaml
# cloud_vars.yml
pv_cloud_init_user: ops
pv_cloud_init_group: ops
pv_cloud_init_hostname: app-server-01
pv_cloud_init_domain: example.com
pv_cloud_init_install_docker: true
pv_cloud_init_authorized_keys:
    - 'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAA...'
```

```bash
ansible-playbook playbooks/cloudinit.yml -i inventory.yml -e @cloud_vars.yml
```

## Inventory Example

```yaml
# inventory.yml
all:
    hosts:
        cloudinit:
            ansible_host: 203.0.113.10
            ansible_user: root
            ansible_ssh_private_key_file: ~/.ssh/id_ed25519
```
