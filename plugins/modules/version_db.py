#!/usr/bin/env python3
import platform

from ansible.module_utils.basic import AnsibleModule
import requests
import jinja2


# "https://api.github.com/repos/gitleaks/gitleaks/releases/latest"
# https://github.com/gitleaks/gitleaks/releases/download/v8.18.3/gitleaks_8.18.3_linux_x64.tar.gz
_SUPPORTED_APPS = {
    "gitleaks": {
        "sha256sum_file_link_template": "https://github.com/gitleaks/gitleaks/releases/download/{{ version }}"
        "/gitleaks_{{ version[1:] }}_checksums.txt",
        "sha256sum_file_name_template": "/gitleaks_{{ version[1:] }}_{{ system }}_{{ arch }}.tar.gz",
        "github_repo": "gitleaks/gitleaks",
        "download_link_template": "https://github.com/gitleaks/gitleaks/releases/download/{{ version }}"
        "/gitleaks_{{ version[1:] }}_{{ system }}_{{ arch }}.tar.gz",
        "arch_map": {
            "x86_64": "x64",
            "aarch64": "arm64",
        },
    }
}

latest_release_res = requests.get(
    f"https://api.github.com/repos/{_SUPPORTED_APPS['gitleaks']['github_repo']}/releases/latest",
    timeout=10,
)

platform_system = platform.system().lower()
platform_arch = platform.machine().lower()

if latest_release_res.status_code != 200:
    print("Failed to fetch latest release")
    exit(1)

latest_release = latest_release_res.json()
print(latest_release["tag_name"])

environment = jinja2.Environment()
template = environment.from_string(_SUPPORTED_APPS["gitleaks"]["download_link_template"])
print(
    template.render(
        version=latest_release["tag_name"],
        system=platform_system,
        arch=_SUPPORTED_APPS["gitleaks"]["arch_map"][platform_arch],
    )
)
