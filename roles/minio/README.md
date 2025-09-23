# Ansible Role: Minio (arpanrec.nebula.minio)

## Minio

This role installs a Minio managed by systemd.

## Variables

| Variable                                           | Type  | Required | Default                          | Description                                                                                                                                  |
| -------------------------------------------------- | ----- | -------- | -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `gitea_cluster_name`                               | `str` | `false`  | `main`                           | Isolated gitea instance.                                                                                                                     |
| `gitea_service_group`                              | `str` | `false`  | `gitea-{{ gitea_cluster_name }}` | Gitea Service Group.                                                                                                                         |
| `gitea_service_user`                               | `str` | `false`  | `{{ gitea_service_group }}`      | Gitea Service User.                                                                                                                          |
| `gitea_rv_version`                                 | `str` | `false`  | `fetch_latest_version`           | If set to `fetch_latest_version` it will pull from [Gitea version](https://github.com/go-gitea/gitea/releases), else something like `1.24.6` |
| `gitea_http_port`                                  | `int` | `false`  | `8582`                           | Http port.                                                                                                                                   |
| `gitea_ssh_port`                                   | `int` | `false`  | `8583`                           | SSH port.                                                                                                                                    |
| `gitea_domain`                                     | `str` | `false`  | `{{ ansible_fqdn }}`             | Gitea communication URI.                                                                                                                     |
| `gitea_http_cert_pem_content`                      | `str` | `false`  | None                             | Gitea SSL Certificate pem content.                                                                                                           |
| `gitea_http_key_pem_content`                       | `str` | `false`  | None                             | Gitea SSL Key pem content.                                                                                                                   |
| `gitea_secret_key`                                 | `str` | `false`  | None                             | Global secret key (Generated automatically if not provided).                                                                                 |
| `gitea_internal_token`                             | `str` | `false`  | None                             | Internal secret within Gitea binary (generated automatically if not provided).                                                               |
| `gitea_oauth2_jwt_secret`                          | `str` | `false`  | None                             | OAuth2 authentication secret (generated automatically if not provided).                                                                      |
| `gitea_lfs_jwt_secret`                             | `str` | `false`  | None                             | LFS authentication secret (generated automatically if not provided).                                                                         |
| `gitea_admin_user_username`                        | `str` | `false`  | None                             | Gitea admin user username.                                                                                                                   |
| `gitea_admin_user_username`                        | `str` | `false`  | None                             | Gitea admin user password.                                                                                                                   |
| `gitea_admin_user_email`                           | `str` | `false`  | None                             | Gitea admin user email address.                                                                                                              |
| `gitea_global_runner_registration_token_file_path` | `str` | `false`  | None                             | Writes the global runner token to this file.                                                                                                 |
| `gitea_admin_token_file_path`                      | `str` | `false`  | None                             | Writes the admin user token to file.                                                                                                         |


### Example Playbook Minio

```yaml
- name: Include Minio role
  ansible.builtin.import_role:
      name: arpanrec.nebula.minio
```

Just write the admin token to file.

```yaml
- name: Just install minio client.
  ansible.builtin.import_role:
      name: arpanrec.nebula.minio
      tasks_from: minio_client.yml
```
