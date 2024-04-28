# Ansible Role: SSHD Hardening (arpanrec.nebula.ssh_hardening)

This role applies basic security settings for personal VPS

## Variables

`ssh_hardening_rv_ssh_port`

- Type: `int`
- Default: `22`
- Required: `false`
- Description: SSHD Server port.

`ssh_hardening_rv_ssh_security_password_authentication`

- Type: `boolean`
- Default: `false`
- Required: `false`
- Description: To disable tunneled clear text passwords.

`ssh_hardening_rv_ssh_security_permit_root_login`

- Type: `boolean`
- Default: `false`
- Required: `false`
- Description: Specifies whether root can log in using ssh.

`ssh_hardening_rv_ssh_security_permit_empty_passwords`

- Type: `boolean`
- Default: `false`
- Required: `false`
- Description: When password authentication is allowed, it specifies whether the server allows login to accounts with empty password strings.

`ssh_hardening_rv_ssh_security_max_auth_tries`

- Type: `int`
- Default: `3`
- Required: `false`
- Description: Specifies the maximum number of authentication attempts permitted per connection. Once the number of failures reaches half this value, additional failures are logged.

`ssh_hardening_rv_ssh_security_x11_forwarding`

- Type: `boolean`
- Default: `false`
- Required: `false`
- Description: Specifies whether X11 forwarding is permitted.

`ssh_hardening_rv_ssh_security_client_alive_interval`

- Type: `int`
- Default: `60`
- Required: `false`
- Description: Sets a timeout interval in seconds after which if no data has been received from the client.

`ssh_hardening_rv_ssh_security_client_alive_count_max`

- Type: `int`
- Default: `3`
- Required: `false`
- Description: Sets the number of client alive messages which may be sent without sshd(8) receiving any messages back from the client. If this threshold is reached while client alive messages are being sent, sshd will disconnect the client, terminating the session.

`ssh_hardening_rv_ssh_security_restart_service`

- Type: `bool`
- Default: `true`
- Required: `false`
- Description: Restart sshd handlers

`ssh_hardening_rv_ssh_security_challenge_response_authentication`

- Type: `bool`
- Default: `false`
- Required: `false`
- Description: Challenge-response passwords (beware issues with some PAM modules and threads)

`ssh_hardening_rv_fail2ban_loglevel`

- Type: `string`
- Default: `INFO`
- Required: `false`
- Description: Log level in fail2ban

`ssh_hardening_rv_fail2ban_logtarget`

- Type: `string`
- Default: `/var/log/fail2ban.log`
- Required: `false`
- Description: Log target in fail2ban

`ssh_hardening_rv_fail2ban_ignoreself`

- Type: `boolean`
- Default: `true`
- Required: `false`
- Description: Ignore self in fail2ban

`ssh_hardening_rv_fail2ban_ignoreips`

- Type: `list`
- Default: `["127.0.0.1/8 ::1"]`
- Required: `false`
- Description: Ignore IPs in fail2ban

`ssh_hardening_rv_fail2ban_bantime`

- Type: `int`
- Default: `600`
- Required: `false`
- Description: Ban time in fail2ban

`ssh_hardening_rv_fail2ban_findtime`

- Type: `int`
- Default: `600`
- Required: `false`
- Description: Find time in fail2ban

`ssh_hardening_rv_fail2ban_maxretry`

- Type: `int`
- Default: `5`
- Required: `false`
- Description: Max retry in fail2ban

`ssh_hardening_rv_fail2ban_destemail`

- Type: `string`
- Default: `root@localhost`
- Required: `false`
- Description: Destination email in fail2ban

`ssh_hardening_rv_fail2ban_sender`

- Type: `string`
- Default: `root@{{ ansible_fqdn }}`
- Required: `false`
- Description: Sender email in fail2ban

`ssh_hardening_rv_fail2ban_configuration`

- Type: `list`
- Default: `[]`
- Required: `false`
- Description: Fail2ban configuration
- Example:

  ```yaml
  ssh_hardening_rv_fail2ban_configuration:
    - option: loglevel
      value: "INFO"
      section: Definition
  ```

`ssh_hardening_rv_fail2ban_jail_configuration`

- Type: `list`
- Default: `[]`
- Required: `false`
- Description: Fail2ban jail configuration
- Example:

  ```yaml
  ssh_hardening_rv_fail2ban_jail_configuration:
    - option: ignoreself
      value: "true"
      section: DEFAULT
  ```

`ssh_hardening_rv_fail2ban_filterd_path`

- Type: `string`
- Default: none
- Required: `false`
- Description: From where to copy the filterd files
  
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
