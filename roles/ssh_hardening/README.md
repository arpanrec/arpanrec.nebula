# Ansible Role: SSH Hardening (arpanrec.nebula.ssh_hardening)

Applies SSH daemon security hardening and deploys [Fail2Ban](https://www.fail2ban.org/) for automated intrusion prevention on servers and VPS instances.

## Features

- SSH daemon (`sshd`) configuration hardening
- Fail2Ban deployment with configurable jail and ban settings
- Brute-force protection with automatic IP banning via nftables (or iptables/ufw)
- Configurable authentication policies: password auth, root login, empty passwords, X11 forwarding
- Idle session timeout via `ClientAliveInterval` and `ClientAliveCountMax`
- Email notification support for security events
- Custom Fail2Ban filter file support

## Requirements

- Debian-based Linux distribution
- Root or sudo privileges on the target host
- `fail2ban` and `nftables` available via apt (installed by this role)

## Variables

### SSH Daemon Settings

| Variable                                                          | Type      | Required | Default | Description                                                                      |
| ----------------------------------------------------------------- | --------- | -------- | ------- | -------------------------------------------------------------------------------- |
| `ssh_hardening_rv_ssh_port`                                       | `int`     | `false`  | `22`    | Port the SSH daemon listens on.                                                  |
| `ssh_hardening_rv_ssh_security_password_authentication`           | `boolean` | `false`  | `false` | Allow password-based authentication. Disabled by default — use key-based auth.   |
| `ssh_hardening_rv_ssh_security_permit_root_login`                 | `boolean` | `false`  | `false` | Allow direct root login via SSH.                                                 |
| `ssh_hardening_rv_ssh_security_permit_empty_passwords`            | `boolean` | `false`  | `false` | Allow login to accounts with empty passwords.                                    |
| `ssh_hardening_rv_ssh_security_max_auth_tries`                    | `int`     | `false`  | `3`     | Maximum authentication attempts per connection before logging and disconnecting. |
| `ssh_hardening_rv_ssh_security_x11_forwarding`                    | `boolean` | `false`  | `false` | Permit X11 forwarding.                                                           |
| `ssh_hardening_rv_ssh_security_client_alive_interval`             | `int`     | `false`  | `60`    | Seconds of inactivity before the server sends a keepalive probe.                 |
| `ssh_hardening_rv_ssh_security_client_alive_count_max`            | `int`     | `false`  | `3`     | Number of unanswered keepalive probes before the session is terminated.          |
| `ssh_hardening_rv_ssh_security_challenge_response_authentication` | `bool`    | `false`  | `false` | Enable challenge-response (PAM-based) authentication.                            |

### Fail2Ban Settings

| Variable                                        | Type      | Required | Default                         | Description                                                                      |
| ----------------------------------------------- | --------- | -------- | ------------------------------- | -------------------------------------------------------------------------------- |
| `ssh_hardening_rv_fail2ban_loglevel`            | `string`  | `false`  | `INFO`                          | Fail2Ban log verbosity (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`).        |
| `ssh_hardening_rv_fail2ban_logtarget`           | `string`  | `false`  | `/var/log/fail2ban.log`         | Log output target (file path, `STDOUT`, `STDERR`, or `SYSLOG`).                  |
| `ssh_hardening_rv_fail2ban_ignoreself`          | `boolean` | `false`  | `true`                          | Prevent Fail2Ban from banning the machine's own IP addresses.                    |
| `ssh_hardening_rv_fail2ban_ignoreips`           | `list`    | `false`  | `["127.0.0.1/8 ::1"]`           | List of IP addresses or CIDR ranges that are never banned.                       |
| `ssh_hardening_rv_fail2ban_banaction`           | `string`  | `false`  | `nftables`                      | Default ban action (`nftables`, `iptables-multiport`, `ufw`, `shorewall`, etc.). |
| `ssh_hardening_rv_fail2ban_banaction_multiport` | `string`  | `false`  | `nftables-multiport`            | Ban action for multi-port jails.                                                 |
| `ssh_hardening_rv_fail2ban_banaction_allports`  | `string`  | `false`  | `nftables-allports`             | Ban action for all-ports jails.                                                  |
| `ssh_hardening_rv_fail2ban_bantime`             | `int`     | `false`  | `86400`                         | Duration (seconds) an IP is banned. Set to `-1` for a permanent ban.             |
| `ssh_hardening_rv_fail2ban_findtime`            | `int`     | `false`  | `600`                           | Time window (seconds) within which `maxretry` failures trigger a ban.            |
| `ssh_hardening_rv_fail2ban_maxretry`            | `int`     | `false`  | `5`                             | Number of failures within `findtime` before an IP is banned.                     |
| `ssh_hardening_rv_fail2ban_destemail`           | `string`  | `false`  | `root@localhost`                | Destination email address for ban notifications.                                 |
| `ssh_hardening_rv_fail2ban_sender`              | `string`  | `false`  | `root@{{ ansible_facts.fqdn }}` | Sender email address for ban notifications.                                      |
| `ssh_hardening_rv_fail2ban_configuration`       | `list`    | `false`  | `[]`                            | Additional Fail2Ban `[Definition]` section options. See example below.           |
| `ssh_hardening_rv_fail2ban_jail_configuration`  | `list`    | `false`  | `[]`                            | Additional Fail2Ban `[DEFAULT]` jail options. See example below.                 |
| `ssh_hardening_rv_fail2ban_filterd_path`        | `string`  | `false`  | -                               | Local path to copy custom Fail2Ban filter files from.                            |

#### `ssh_hardening_rv_fail2ban_configuration` format

```yaml
ssh_hardening_rv_fail2ban_configuration:
    - option: 'loglevel'
      value: 'DEBUG'
      section: 'Definition'
```

#### `ssh_hardening_rv_fail2ban_jail_configuration` format

```yaml
ssh_hardening_rv_fail2ban_jail_configuration:
    - option: 'ignoreself'
      value: 'true'
      section: 'DEFAULT'
```

## Example Playbook

Minimal hardening with key-only SSH access:

```yaml
- name: Harden SSH
  hosts: all
  roles:
      - name: arpanrec.nebula.ssh_hardening
```

Allow password authentication (e.g., during initial provisioning):

```yaml
- name: Harden SSH
  hosts: all
  roles:
      - name: arpanrec.nebula.ssh_hardening
        vars:
            ssh_hardening_rv_ssh_port: 2222
            ssh_hardening_rv_ssh_security_password_authentication: true
            ssh_hardening_rv_fail2ban_bantime: -1
            ssh_hardening_rv_fail2ban_ignoreips:
                - '127.0.0.1/8 ::1'
                - '10.0.0.0/8'
```

## Testing

```bash
molecule test -s role.ssh_hardening.default
```
