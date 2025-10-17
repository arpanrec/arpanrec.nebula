# Ansible Role: Minio (arpanrec.nebula.minio)

## Minio

This role installs a Minio managed by systemd.

## Variables

| Variable                        | Type | Required | Default                                        | Description                                                           |
| ------------------------------- | ---- | -------- | ---------------------------------------------- | --------------------------------------------------------------------- |
| `minio_cluster_name`            | str  | false    | `main`                                         | Isolated MinIO instance name.                                         |
| `minio_service_group`           | str  | false    | `minio-{{ minio_cluster_name }}`               | System group that owns the MinIO service.                             |
| `minio_service_user`            | str  | false    | `{{ minio_service_group }}`                    | System user that runs the MinIO service.                              |
| `minio_rv_version`              | str  | false    | `fetch_latest_version`                         | MinIO server version to install. Like `RELEASE.2025-09-07T16-13-09Z`  |
| `minio_client_rv_version`       | str  | false    | `fetch_latest_version`                         | MinIO client (mc) version to install.                                 |
| `minio_rv_s3_port`              | int  | false    | `9000`                                         | S3 API listening port.                                                |
| `minio_rv_console_port`         | int  | false    | `9001`                                         | MinIO web console port.                                               |
| `minio_rv_directory`            | str  | false    | `/etc/minio/{{ minio_cluster_name }}`          | Configuration directory path.                                         |
| `minio_rv_data_directory`       | str  | false    | `/var/lib/minio/{{ minio_cluster_name }}/data` | Data directory path.                                                  |
| `minio_root_user`               | str  | false    | `minio-root-{{ minio_cluster_name }}`          | Root access key/username for MinIO.                                   |
| `minio_root_password`           | str  | false    | Generated (40 chars, lowercase+digits)         | Root secret key/password; generated at runtime.                       |
| `minio_server_cert_pem_content` | str  | false    | —                                              | PEM-encoded server certificate for TLS (set if TLS enabled).          |
| `minio_server_key_pem_content`  | str  | false    | —                                              | PEM-encoded server private key for TLS (set if TLS enabled).          |
| `minio_server_ca_pem_content`   | str  | false    | —                                              | PEM-encoded CA bundle for TLS trust chain (optional, for custom CAs). |

### Example Playbook Minio

```yaml
- name: Include Minio role
  ansible.builtin.import_role:
      name: arpanrec.nebula.minio
```

```yaml
- name: Just install minio client.
  ansible.builtin.import_role:
      name: arpanrec.nebula.minio
      tasks_from: minio_client.yml
```
