# Ansible Role: SSHD Hardening (arpanrec.nebula.ssh_hardening)

This role implements comprehensive SSH security hardening and intrusion detection for servers and VPS instances. It configures SSH daemon security settings and deploys Fail2Ban for automated threat mitigation.

**Features:**

- SSH daemon security configuration and hardening
- Fail2Ban intrusion detection and prevention system
- Configurable authentication policies and limits
- Brute force protection with automatic IP banning
- Email notifications for security events
- Customizable firewall integration (UFW, iptables, etc.)
- Comprehensive logging and monitoring
- Support for custom security policies and configurations

This role applies basic security settings for personal VPS

## Variables

| Variable                                                          | Type      | Required | Default                   | Description                                                                                                                                                                                                                                                |
| ----------------------------------------------------------------- | --------- | -------- | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ssh_hardening_rv_ssh_port`                                       | `int`     | `false`  | `22`                      | SSHD Server port.                                                                                                                                                                                                                                          |
| `ssh_hardening_rv_ssh_security_password_authentication`           | `boolean` | `false`  | `false`                   | To disable tunneled clear text passwords.                                                                                                                                                                                                                  |
| `ssh_hardening_rv_ssh_security_permit_root_login`                 | `boolean` | `false`  | `false`                   | Specifies whether root can log in using ssh.                                                                                                                                                                                                               |
| `ssh_hardening_rv_ssh_security_permit_empty_passwords`            | `boolean` | `false`  | `false`                   | When password authentication is allowed, it specifies whether the server allows login to accounts with empty password strings.                                                                                                                             |
| `ssh_hardening_rv_ssh_security_max_auth_tries`                    | `int`     | `false`  | `3`                       | Specifies the maximum number of authentication attempts permitted per connection. Once the number of failures reaches half this value, additional failures are logged.                                                                                     |
| `ssh_hardening_rv_ssh_security_x11_forwarding`                    | `boolean` | `false`  | `false`                   | Specifies whether X11 forwarding is permitted.                                                                                                                                                                                                             |
| `ssh_hardening_rv_ssh_security_client_alive_interval`             | `int`     | `false`  | `60`                      | Sets a timeout interval in seconds after which if no data has been received from the client.                                                                                                                                                               |
| `ssh_hardening_rv_ssh_security_client_alive_count_max`            | `int`     | `false`  | `3`                       | Sets the number of client alive messages which may be sent without sshd(8) receiving any messages back from the client. If this threshold is reached while client alive messages are being sent, sshd will disconnect the client, terminating the session. |
| `ssh_hardening_rv_ssh_security_challenge_response_authentication` | `bool`    | `false`  | `false`                   | Challenge-response passwords (beware issues with some PAM modules and threads)                                                                                                                                                                             |
| `ssh_hardening_rv_fail2ban_loglevel`                              | `string`  | `false`  | `INFO`                    | Log level in fail2ban                                                                                                                                                                                                                                      |
| `ssh_hardening_rv_fail2ban_logtarget`                             | `string`  | `false`  | `/var/log/fail2ban.log`   | Log target in fail2ban                                                                                                                                                                                                                                     |
| `ssh_hardening_rv_fail2ban_ignoreself`                            | `boolean` | `false`  | `true`                    | Ignore self in fail2ban                                                                                                                                                                                                                                    |
| `ssh_hardening_rv_fail2ban_ignoreips`                             | `list`    | `false`  | `["127.0.0.1/8 ::1"]`     | Ignore IPs in fail2ban                                                                                                                                                                                                                                     |
| `ssh_hardening_rv_fail2ban_banaction`                             | `string`  | `false`  | `nftables`                | Ban action in fail2ban, like iptables-multiport, iptables-allports, ufw, nftables, shorewall, etc.                                                                                                                                                         |
| `ssh_hardening_rv_fail2ban_banaction_multiport`                   | `string`  | `false`  | `nftables-multiport`      | Ban action in fail2ban, like iptables-multiport, iptables-allports, ufw, nftables, shorewall, etc.                                                                                                                                                         |
| `ssh_hardening_rv_fail2ban_banaction_allports`                    | `string`  | `false`  | `nftables-allports`       | Ban action in fail2ban, like iptables-multiport, iptables-allports, ufw, nftables, shorewall, etc.                                                                                                                                                         |
| `ssh_hardening_rv_fail2ban_bantime`                               | `int`     | `false`  | `86400`                   | Ban time in fail2ban. For permanent ban, set it to -1                                                                                                                                                                                                      |
| `ssh_hardening_rv_fail2ban_findtime`                              | `int`     | `false`  | `600`                     | Find time in fail2ban                                                                                                                                                                                                                                      |
| `ssh_hardening_rv_fail2ban_maxretry`                              | `int`     | `false`  | `5`                       | Max retry in fail2ban                                                                                                                                                                                                                                      |
| `ssh_hardening_rv_fail2ban_destemail`                             | `string`  | `false`  | `root@localhost`          | Destination email in fail2ban                                                                                                                                                                                                                              |
| `ssh_hardening_rv_fail2ban_sender`                                | `string`  | `false`  | `root@{{ ansible_facts.fqdn }}` | Sender email in fail2ban                                                                                                                                                                                                                                   |
| `ssh_hardening_rv_fail2ban_configuration`                         | `list`    | `false`  | `[]`                      | Fail2ban configuration. Example: `[{option: "loglevel", value: "INFO", section: "Definition"}]`                                                                                                                                                            |
| `ssh_hardening_rv_fail2ban_jail_configuration`                    | `list`    | `false`  | `[]`                      | Fail2ban jail configuration. Example: `[{option: "ignoreself", value: "true", section: "DEFAULT"}]`                                                                                                                                                        |
| `ssh_hardening_rv_fail2ban_filterd_path`                          | `string`  | `false`  | -                         | From where to copy the filterd files                                                                                                                                                                                                                       |

## Example Playbook

```yaml
- name: SSHD Hardening
  ansible.builtin.import_role:
      name: arpanrec.nebula.ssh_hardening
  vars:
      ssh_hardening_rv_ssh_security_password_authentication: true
```

## Testing

```bash
molecule test -s role.ssh_hardening.default
```
