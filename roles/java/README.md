# Ansible Role: Server Workspace (arpanrec.nebula.server_workspace)

## Oracle Java

Install oracle jdk in user space

## Variables

```yaml
options:
    java_rv_jdk_tmp_dir:
        description: Temporary directory.
        required: false
        type: str
        default: "{{ ansible_facts.user_dir }}/.tmp/java"
    java_rv_jdk_install_path:
        description: Install path for java.
        required: false
        type: str
        default: "{{ pv_ua_user_share_dir }}/java"
    java_rv_jdk_version:
        description:
            - Example format `21.0.4`
            - If set to `fetch_latest_version` then the latest version will be installed.
        required: false
        type: str
        default: fetch_latest_version
    java_rv_jdk_mvn_install_path:
        description: Install Path.
        required: false
        type: str
        default: "{{ pv_ua_user_share_dir }}/maven"
    java_rv_jdk_mvn_version:
        description:
            - Exact release version of maven.
            - Example format `maven-3.8.4`
            - If set to `fetch_latest_version` then the latest version will be installed.
        required: false
        default: fetch_latest_version
        type: str
    java_rv_jdk_gradle_version:
        description:
            - Release version of Gradle from https://gradle.org/releases/.
            - Example format `v7.6.4`
            - If set to `fetch_latest_version` then the latest version will be installed.
        required: false
        default: fetch_latest_version
        type: str
    java_rv_jdk_groovy_version:
        description: 
            - Release version of Groovy from https://groovy.apache.org/download.html.
            - If set to `fetch_latest_version` then the latest version will be installed.
            - Example format `4.0.22`
        required: false
        type: str
        default: "fetch_latest_version"
    java_rv_jdk_kotlinc_version:
        description:
            - Release version of Kotlin
            - Example format `v2.0.21`
            - If set to `fetch_latest_version` then the latest version will be installed.
        required: false
        default: fetch_latest_version
        type: str
    java_rv_jdk_graalvm_install_path:
        description: Install Path for [GraalVM](https://www.graalvm.org/).
        required: false
        type: str
        default: "{{ ansible_facts.user_dir }}/.local/share/graalvm"
```

## Example Playbook Oracle Java

```yaml
- name: Oracle JDK
  hosts: all
  roles:
      - name: arpanrec.nebula.java
```

## Testing Oracle Java

```bash
molecule test -s role.java.default
```
