# Ansible Collection: arpanrec.nebula

An Ansible collection providing roles for infrastructure automation and development environment setup on Debian-based systems.

- **Namespace:** `arpanrec`
- **Collection:** `nebula`
- **Version:** 1.14.66
- **License:** MIT
- **Minimum Ansible Version:** 2.10

## Installation

```bash
ansible-galaxy collection install "git+https://github.com/arpanrec/arpanrec.nebula.git,1.14.66"
```

Or via requirements file:

```yaml
# requirements.yml
collections:
    - name: https://github.com/arpanrec/arpanrec.nebula.git
      type: git
      version: 1.14.66
```

```bash
ansible-galaxy collection install -r requirements.yml
```

## Dependencies

| Collection             | Version  |
| ---------------------- | -------- |
| `community.general`    | `12.3.0` |
| `community.crypto`     | `3.1.0`  |
| `ansible.posix`        | `2.1.0`  |
| `community.postgresql` | `4.2.0`  |

## Roles

### Programming Languages & Runtimes

| Role                             | Description                                            |
| -------------------------------- | ------------------------------------------------------ |
| [go](roles/go/README.md)         | Go programming language runtime and development tools  |
| [java](roles/java/README.md)     | Oracle JDK, Maven, Gradle, Groovy, Kotlin, and GraalVM |
| [nodejs](roles/nodejs/README.md) | Node.js runtime with global package management         |

### Infrastructure as Code

| Role                                   | Description                            |
| -------------------------------------- | -------------------------------------- |
| [terraform](roles/terraform/README.md) | HashiCorp Terraform CLI                |
| [pulumi](roles/pulumi/README.md)       | Pulumi infrastructure-as-code platform |

### Security & Secrets Management

| Role                                           | Description                                            |
| ---------------------------------------------- | ------------------------------------------------------ |
| [vault](roles/vault/README.md)                 | HashiCorp Vault CLI for secrets management             |
| [bws](roles/bws/README.md)                     | Bitwarden Secrets Manager SDK CLI                      |
| [ssh_hardening](roles/ssh_hardening/README.md) | SSH daemon hardening and Fail2Ban intrusion prevention |
| [gitleaks](roles/gitleaks/README.md)           | Secret detection in git repositories and files         |

### Code Quality

| Role                                 | Description                                   |
| ------------------------------------ | --------------------------------------------- |
| [hadolint](roles/hadolint/README.md) | Dockerfile linter with ShellCheck integration |

### Services & Databases

| Role                                     | Description                                                           |
| ---------------------------------------- | --------------------------------------------------------------------- |
| [postgresql](roles/postgresql/README.md) | PostgreSQL server with systemd management, SSL, and user provisioning |
| [gitea](roles/gitea/README.md)           | Self-hosted Gitea Git service with systemd management                 |

### System Administration

| Role                                             | Description                                                          |
| ------------------------------------------------ | -------------------------------------------------------------------- |
| [linux_patching](roles/linux_patching/README.md) | Debian system patching, package management, and system configuration |
| [user_add](roles/user_add/README.md)             | User account creation with SSH access and sudo configuration         |

## Playbooks

| Playbook                                          | Description                                                                                                 |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| [server_workspace](playbooks/server_workspace.md) | Complete developer workstation setup (Go, Node.js, Java, Terraform, Vault, Pulumi, BWS, Hadolint, Gitleaks) |
| [cloudinit](playbooks/cloudinit.md)               | Cloud instance initialization (user provisioning, system setup, optional Docker)                            |

## Plugins

### Lookup Plugins

| Plugin                                     | Description                                                                                                                        |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| [bitwarden](plugins/lookup/bitwarden.py)   | Retrieve secrets from a Bitwarden vault using the `bw` CLI with caching support                                                    |
| [version_db](plugins/lookup/version_db.py) | Fetch the latest release version for supported tools (Go, Node.js, Java, Terraform, Vault, Pulumi, BWS, Gitleaks, Hadolint, Gitea) |

### Filter Plugins

| Plugin                                                     | Description                                                                     |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------- |
| [split_certificates](plugins/filter/split_certificates.py) | Split a concatenated PEM certificate bundle into individual certificate entries |

## Version Detection

Roles that install versioned binaries support automatic latest-version detection. Set any `*_version` variable to `fetch_latest_version` (the default) and the `version_db` lookup plugin will query the appropriate upstream API (GitHub Releases or HashiCorp Releases) to resolve the latest stable version at play time.

To pin a specific version, provide the exact version string:

```yaml
- name: Install Go
  ansible.builtin.import_role:
      name: arpanrec.nebula.go
  vars:
      go_rv_version: 'go1.23.2'
```

## License

[MIT](LICENSE)
