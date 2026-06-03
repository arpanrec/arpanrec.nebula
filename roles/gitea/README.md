# Ansible Role: Gitea (arpanrec.nebula.gitea)

Installs and configures a self-hosted [Gitea](https://gitea.com/) Git service managed by systemd. Supports PostgreSQL backends, SSL/TLS, OAuth2, Git LFS, and multiple isolated instances on the same host.

## Features

- Gitea installation with automatic latest-version detection via GitHub Releases
- systemd service management with a dedicated service user and group
- SSL/TLS support for HTTPS and built-in SSH server
- PostgreSQL backend with optional SSL client certificate authentication
- OAuth2 JWT and LFS JWT secret management (auto-generated if not provided)
- Multiple isolated cluster instances via `gitea_cluster_name`
- Admin user provisioning and API token export

## Requirements

- Debian-based Linux distribution
- Root or sudo privileges on the target host
- A running PostgreSQL instance when using `gitea_config_db_postgresql`

## Variables

### Core Variables

| Variable                            | Type  | Required | Default                                                           | Description                                                                                           |
| ----------------------------------- | ----- | -------- | ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `gitea_cluster_name`                | `str` | `false`  | `main`                                                            | Logical name for this Gitea instance. Used to namespace data directories and systemd units.           |
| `gitea_working_directory`           | `str` | `false`  | `/var/lib/gitea/{{ gitea_cluster_name }}`                         | Root data directory for this Gitea instance.                                                          |
| `gitea_service_group`               | `str` | `false`  | `gitea-{{ gitea_cluster_name }}`                                  | System group that owns the Gitea process.                                                             |
| `gitea_service_user`                | `str` | `false`  | `{{ gitea_service_group }}`                                       | System user that runs the Gitea process.                                                              |
| `gitea_service_user_home_directory` | `str` | `false`  | `{{ gitea_working_directory }}`                                   | Home directory for the Gitea service user.                                                            |
| `gitea_rv_version`                  | `str` | `false`  | `fetch_latest_version`                                            | Gitea release version. Set to `fetch_latest_version` to resolve the latest from GitHub automatically. |
| `gitea_http_port`                   | `int` | `false`  | `8582`                                                            | Port Gitea's HTTP/HTTPS server listens on.                                                            |
| `gitea_ssh_port`                    | `int` | `false`  | `8583`                                                            | Port Gitea's built-in SSH server listens on.                                                          |
| `gitea_domain`                      | `str` | `false`  | `{{ ansible_facts.fqdn }}`                                        | Public domain name used in clone URLs and web UI.                                                     |
| `gitea_ssh_domain`                  | `str` | `false`  | `{{ gitea_domain }}`                                              | Domain used in SSH clone URLs (can differ from HTTP domain, e.g., behind a reverse proxy).            |
| `gitea_local_root_url`              | `str` | `false`  | `{{ gitea_protocol }}://{{ gitea_domain }}:{{ gitea_http_port }}` | Internal URL used by Gitea workers (e.g., SSH post-receive hooks calling the web API).                |
| `gitea_root_url`                    | `str` | `false`  | `{{ gitea_local_root_url }}`                                      | External URL shown to users. Override when behind a reverse proxy with a different external address.  |
| `gitea_ssh_server_user`             | `str` | `false`  | `{{ gitea_service_user }}`                                        | Username for the built-in SSH server.                                                                 |

### SSL / TLS Variables

| Variable                      | Type  | Required | Default | Description                           |
| ----------------------------- | ----- | -------- | ------- | ------------------------------------- |
| `gitea_http_cert_pem_content` | `str` | `false`  | -       | PEM content of the HTTPS certificate. |
| `gitea_http_key_pem_content`  | `str` | `false`  | -       | PEM content of the HTTPS private key. |

### Security / Authentication Variables

| Variable                  | Type  | Required | Default        | Description                                                    |
| ------------------------- | ----- | -------- | -------------- | -------------------------------------------------------------- |
| `gitea_secret_key`        | `str` | `false`  | auto-generated | Global secret key used for CSRF protection and cookie signing. |
| `gitea_internal_token`    | `str` | `false`  | auto-generated | Internal secret used between Gitea binary instances.           |
| `gitea_oauth2_jwt_secret` | `str` | `false`  | auto-generated | Secret used to sign OAuth2 JWT tokens.                         |
| `gitea_lfs_jwt_secret`    | `str` | `false`  | auto-generated | Secret used to sign LFS JWT tokens.                            |

### Admin User Variables

| Variable                                           | Type  | Required | Default | Description                                                                   |
| -------------------------------------------------- | ----- | -------- | ------- | ----------------------------------------------------------------------------- |
| `gitea_admin_user_username`                        | `str` | `false`  | -       | Username of the initial admin account to create.                              |
| `gitea_admin_user_password`                        | `str` | `false`  | -       | Password for the initial admin account.                                       |
| `gitea_admin_user_email`                           | `str` | `false`  | -       | Email address for the initial admin account.                                  |
| `gitea_global_runner_registration_token_file_path` | `str` | `false`  | -       | If set, the global Actions runner registration token is written to this file. |
| `gitea_admin_token_file_path`                      | `str` | `false`  | -       | If set, the admin user's API token is written to this file.                   |

### `gitea_config_db_postgresql`

PostgreSQL database configuration. See the [Gitea config cheat sheet](https://docs.gitea.com/administration/config-cheat-sheet#database-database) for details.

```yaml
gitea_config_db_postgresql:
    host: '127.0.0.1:5432'
    name: 'gitea'
    user: 'gitea'
    passwd: 'secret'
    schema: 'public'
    ssl_mode: 'disable' # disable, require, verify-ca, verify-full
    pg_ssl_root_cert_pem_content: '' # PEM content of the CA certificate
    pg_ssl_client_cert_pem_content: '' # PEM content of the client certificate
    pg_ssl_client_key_pem_content: '' # PEM content of the client private key
```

SSL certificate files are written to:

```
{{ gitea_service_user_home_directory }}/.postgresql/root.crt
{{ gitea_service_user_home_directory }}/.postgresql/postgresql.crt
{{ gitea_service_user_home_directory }}/.postgresql/postgresql.key
```

### `gitea_extra_config`

Arbitrary Gitea INI configuration options. See the [full config cheat sheet](https://docs.gitea.com/administration/config-cheat-sheet).

```yaml
gitea_extra_config:
    - section: 'server'
      option: 'DISABLE_REGISTRATION'
      value: 'true'
    - section: 'mailer'
      option: 'ENABLED'
      value: 'true'
```

## Example Playbook

Minimal install:

```yaml
- name: Install Gitea
  hosts: all
  roles:
      - name: arpanrec.nebula.gitea
```

With PostgreSQL backend and admin provisioning:

```yaml
- name: Install Gitea with PostgreSQL
  hosts: all
  roles:
      - name: arpanrec.nebula.gitea
        vars:
            gitea_domain: 'git.example.com'
            gitea_admin_user_username: 'admin'
            gitea_admin_user_password: 'changeme'
            gitea_admin_user_email: 'admin@example.com'
            gitea_config_db_postgresql:
                host: '127.0.0.1:5432'
                name: 'gitea'
                user: 'gitea'
                passwd: 'dbpassword'
                ssl_mode: 'disable'
```

Write the admin API token to a file for use in downstream tasks:

```yaml
- name: Gitea | Create temp file for admin token
  ansible.builtin.tempfile:
      state: file
      suffix: .txt
  register: __gitea_admin_token_file

- name: Gitea | Write admin token
  ansible.builtin.import_role:
      name: arpanrec.nebula.gitea
      tasks_from: admin-token.yml
  vars:
      gitea_admin_token_file_path: '{{ __gitea_admin_token_file.path }}'
      gitea_admin_user_username: 'admin'
```

## Backup

All instance data is stored under `gitea_working_directory` (default: `/var/lib/gitea/{{ gitea_cluster_name }}`). Back up this directory to preserve repositories, configuration, and SSL certificates.
