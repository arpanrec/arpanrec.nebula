# Ansible Role: Java (arpanrec.nebula.java)

Installs a complete Java development ecosystem in user space: Oracle JDK, Maven, Gradle, Groovy, Kotlin, and optionally GraalVM.

## Features

- User-space installation (no root privileges required)
- Automatic latest-version detection for all components
- Optional GraalVM installation in place of the standard JDK
- Each component is independently versioned and path-configurable

## Requirements

- Debian-based Linux distribution
- `tar` and `unzip` available on the target host
- Internet access to download from Oracle and GitHub release APIs

## Variables

| Variable                           | Type   | Required | Default                                             | Example   | Description                                                                                                |
| ---------------------------------- | ------ | -------- | --------------------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------- |
| `java_rv_jdk_install_path`         | `str`  | `false`  | `{{ ansible_facts.user_dir }}/.local/share/java`    | -         | Directory where the JDK is extracted.                                                                      |
| `java_rv_jdk_version`              | `str`  | `false`  | `fetch_latest_version`                              | `21.0.4`  | JDK version. Set to `fetch_latest_version` to resolve the latest Oracle JDK release automatically.         |
| `java_rv_jdk_tmp_dir`              | `str`  | `false`  | `{{ ansible_facts.user_dir }}/.tmp/java`            | -         | Temporary directory used during download and extraction.                                                   |
| `java_rv_jdk_mvn_install_path`     | `str`  | `false`  | `{{ ansible_facts.user_dir }}/.local/share/maven`   | -         | Directory where Maven is extracted.                                                                        |
| `java_rv_jdk_mvn_version`          | `str`  | `false`  | `fetch_latest_version`                              | `3.9.6`   | Maven version. Set to `fetch_latest_version` to resolve the latest release automatically.                  |
| `java_rv_jdk_gradle_version`       | `str`  | `false`  | `fetch_latest_version`                              | `8.7`     | Gradle version. Set to `fetch_latest_version` to resolve the latest from gradle.org automatically.         |
| `java_rv_jdk_groovy_version`       | `str`  | `false`  | `fetch_latest_version`                              | `4.0.22`  | Apache Groovy version. Set to `fetch_latest_version` to resolve the latest release automatically.          |
| `java_rv_jdk_kotlinc_version`      | `str`  | `false`  | `fetch_latest_version`                              | `v2.0.21` | Kotlin compiler version. Set to `fetch_latest_version` to resolve the latest GitHub release automatically. |
| `java_rv_jdk_graalvm_install_path` | `str`  | `false`  | `{{ ansible_facts.user_dir }}/.local/share/graalvm` | -         | Directory where GraalVM is extracted (only used when `java_rv_jdk_graalvm_is_install` is `true`).          |
| `java_rv_jdk_graalvm_is_install`   | `bool` | `false`  | `false`                                             | `true`    | When `true`, installs GraalVM instead of the standard Oracle JDK.                                          |

## Example Playbook

```yaml
- name: Install Java ecosystem
  hosts: all
  roles:
      - name: arpanrec.nebula.java
```

Install GraalVM instead of the standard JDK:

```yaml
- name: Install Java with GraalVM
  hosts: all
  roles:
      - name: arpanrec.nebula.java
        vars:
            java_rv_jdk_graalvm_is_install: true
```

Pin specific versions:

```yaml
- name: Install Java ecosystem (pinned)
  hosts: all
  roles:
      - name: arpanrec.nebula.java
        vars:
            java_rv_jdk_version: '21.0.4'
            java_rv_jdk_mvn_version: '3.9.6'
            java_rv_jdk_gradle_version: '8.7'
```

## Testing

```bash
molecule test -s role.java.default
```
