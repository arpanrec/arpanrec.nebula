#!/usr/bin/env python3

# "https://api.github.com/repos/gitleaks/gitleaks/releases/latest"
# https://github.com/gitleaks/gitleaks/releases/download/v8.18.3/gitleaks_8.18.3_linux_x64.tar.gz
from typing import Dict

SUPPORTED_APPS: Dict[str, any] = {
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
