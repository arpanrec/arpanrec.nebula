# Playbook: Server Workspace (server_workspace.yml)

Sets up a complete developer workstation with a curated set of languages, runtimes, and tooling. All tools are installed in user space — no root access required after the play runs.

## Target Host Group

```
server_workspace
```

Define this group in your Ansible inventory pointing at your workstation or remote dev server.

## Included Roles

Each role is tagged with its name, so you can run a subset of roles using `--tags`.

| Tag         | Role                                                      | What it installs                          |
| ----------- | --------------------------------------------------------- | ----------------------------------------- |
| `nodejs`    | [arpanrec.nebula.nodejs](../roles/nodejs/README.md)       | Node.js runtime and global npm packages   |
| `go`        | [arpanrec.nebula.go](../roles/go/README.md)               | Go runtime, gopls, gosh, lazygit          |
| `java`      | [arpanrec.nebula.java](../roles/java/README.md)           | Oracle JDK, Maven, Gradle, Groovy, Kotlin |
| `terraform` | [arpanrec.nebula.terraform](../roles/terraform/README.md) | Terraform CLI                             |
| `vault`     | [arpanrec.nebula.vault](../roles/vault/README.md)         | HashiCorp Vault CLI                       |
| `pulumi`    | [arpanrec.nebula.pulumi](../roles/pulumi/README.md)       | Pulumi CLI                                |
| `bws`       | [arpanrec.nebula.bws](../roles/bws/README.md)             | Bitwarden Secrets Manager CLI             |
| `hadolint`  | [arpanrec.nebula.hadolint](../roles/hadolint/README.md)   | Dockerfile linter                         |
| `gitleaks`  | [arpanrec.nebula.gitleaks](../roles/gitleaks/README.md)   | Secret detection tool                     |

All roles are enabled by default. Use `--tags` to run only specific tools, or `--skip-tags` to exclude them.

## Usage

Run the full workspace setup:

```bash
ansible-playbook playbooks/server_workspace.yml -i inventory.yml
```

Install only Go and Node.js:

```bash
ansible-playbook playbooks/server_workspace.yml -i inventory.yml --tags "go,nodejs"
```

Skip Java (e.g., on a lightweight machine):

```bash
ansible-playbook playbooks/server_workspace.yml -i inventory.yml --skip-tags java
```

## Extra Variables

Role variables can be passed via `--extra-vars` or a vars file and are forwarded directly to the underlying roles.

```bash
ansible-playbook playbooks/server_workspace.yml -i inventory.yml \
  --extra-vars "go_rv_version=go1.23.2 nodejs_rv_version=v22.9.0"
```

See each role's README for the full list of supported variables.

## Inventory Example

```yaml
# inventory.yml
all:
    hosts:
        server_workspace:
            ansible_host: 192.168.1.100
            ansible_user: deploy
```
