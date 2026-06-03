# Ansible Role: PostgreSQL (arpanrec.nebula.postgresql)

Installs and configures a [PostgreSQL](https://www.postgresql.org/) server managed by systemd and `pg_ctlcluster`. Supports SSL/TLS, custom HBA rules, user provisioning, database creation, and privilege management.

## Features

- PostgreSQL server installation from the official apt repository
- systemd service management via `pg_ctlcluster`
- SSL/TLS support with configurable certificates
- Custom `pg_hba.conf` and `postgresql.conf` options
- User and database provisioning
- Fine-grained privilege assignment

## Requirements

- Debian-based Linux distribution
- Root or sudo privileges on the target host
- `community.postgresql` collection (version `4.2.0+`)

## Variables

### Core Variables

| Variable                          | Type  | Required | Default | Description                                                               |
| --------------------------------- | ----- | -------- | ------- | ------------------------------------------------------------------------- |
| `postgresql_version`              | `str` | `false`  | `17`    | PostgreSQL major version to install.                                      |
| `postgresql_cluster`              | `str` | `false`  | `main`  | Cluster name (passed to `pg_ctlcluster`).                                 |
| `postgresql_port`                 | `int` | `false`  | `5432`  | Port the PostgreSQL server listens on.                                    |
| `postgresql_super_user_password`  | `str` | `false`  | -       | Password for the `postgres` superuser. Leave unset to keep the default.   |
| `postgresql_ssl_cert_pem_content` | `str` | `false`  | -       | PEM content of the server SSL certificate.                                |
| `postgresql_ssl_key_pem_content`  | `str` | `false`  | -       | PEM content of the server SSL private key.                                |
| `postgresql_ssl_ca_pem_content`   | `str` | `false`  | -       | PEM content of the CA certificate used for client certificate validation. |

### `postgresql_extra_hba_rules`

Additional rules appended to `pg_hba.conf`. Default rules are defined in `vars/main.yml` — custom entries may conflict with them.

```yaml
postgresql_extra_hba_rules:
    - contype: hostssl # local, host, hostssl, hostnossl
      databases: mydb
      users: myuser
      method: scram-sha-256 # md5, peer, scram-sha-256, cert
      options: '' # e.g. clientcert=verify-full
```

### `postgresql_extra_conf_options`

Additional key/value pairs appended to `postgresql.conf`. Default options are defined in `vars/main.yml`.

```yaml
postgresql_extra_conf_options:
    - option: max_connections
      value: '200'
    - option: work_mem
      value: "'64MB'" # wrap complex values in single quotes
```

### `postgresql_users`

Users to ensure exist in the cluster.

```yaml
postgresql_users:
    - name: myuser # required
      password: secret # optional
      encrypted: true # optional; defaults to not set
      role_attr_flags: CREATEDB # optional
      state: present # optional; defaults to present
```

### `postgresql_databases`

Databases to ensure exist in the cluster.

```yaml
postgresql_databases:
    - name: mydb # required
      owner: myuser # optional; defaults to postgresql_user
      encoding: UTF-8 # optional; defaults to UTF-8
      lc_collate: en_US.UTF-8 # optional
      lc_ctype: en_US.UTF-8 # optional
      template: template0 # optional
      state: present # optional; defaults to present
```

### `postgresql_privs`

Privilege grants on database objects. See the [community.postgresql.postgresql_privs module docs](https://docs.ansible.com/ansible/latest/collections/community/postgresql/postgresql_privs_module.html) for all options.

```yaml
postgresql_privs:
    - login_db: mydb # required
      roles: myuser # required
      privs: SELECT,INSERT # optional
      type: table # optional
      objs: mytable # optional
      schema: public # optional
      state: present # optional; defaults to present
```

## Example Playbook

Minimal install:

```yaml
- name: Install PostgreSQL
  hosts: all
  roles:
      - name: arpanrec.nebula.postgresql
```

Full example with SSL, a user, and a database:

```yaml
- name: Install PostgreSQL with SSL and provisioning
  hosts: all
  roles:
      - name: arpanrec.nebula.postgresql
        vars:
            postgresql_version: '17'
            postgresql_port: 5432
            postgresql_super_user_password: 'changeme'
            postgresql_ssl_cert_pem_content: "{{ lookup('file', 'server.crt') }}"
            postgresql_ssl_key_pem_content: "{{ lookup('file', 'server.key') }}"
            postgresql_users:
                - name: appuser
                  password: apppassword
            postgresql_databases:
                - name: appdb
                  owner: appuser
```

## Backup

All cluster data lives under `postgresql_working_directory` (default: `/var/lib/postgresql/<version>/<cluster>`). Back up that directory to preserve all databases, configuration, and SSL certificates.
