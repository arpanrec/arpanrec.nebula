# Ansible Role: Utils (arpanrec.nebula.utils)

This role provides utility functions and helper tasks for common operations across other Ansible roles. It includes reusable tasks for certificate management, secret handling, and other shared functionality.

**Features:**

- TLS certificate management utilities
- Secret and environment variable handling
- Reusable task modules for other roles
- Common helper functions and utilities
- Standardized error handling and logging

Helper Ansible Roles

## TLS Certificate `tlscert.yml`

```yaml
- name: "Include tasks from set_secret_vault_env"
    import_role:
    name: arpanrec.utils
    tasks_from: tlscert.yml
```

## Test

```yaml
git clone git@github.com:arpanrec/ansible-role-utils.git arpanrec.utils
cd arpanrec.utils
python3 -m pip install --user --upgrade pip
python3 -m pip install --user --upgrade wheel setuptools
python3 -m pip install --user --upgrade virtualenv
virtualenv --python $(readlink -f $(which python3)) venv
source venv/bin/activate
venv/bin/python3 -m pip install -r .github/files/requirements.txt --upgrade
molecule test
```
