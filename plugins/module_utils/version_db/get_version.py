import requests
import platform
import sys
import jinja2

from . import SUPPORTED_APPS


def get_version():
    latest_release_res = requests.get(
        f"https://api.github.com/repos/{SUPPORTED_APPS['gitleaks']['github_repo']}/releases/latest",
        timeout=10,
    )

    platform_system = platform.system().lower()
    platform_arch = platform.machine().lower()

    if latest_release_res.status_code != 200:
        print("Failed to fetch latest release")
        sys.exit(1)

    latest_release = latest_release_res.json()
    print(latest_release["tag_name"])

    environment = jinja2.Environment()
    template = environment.from_string(SUPPORTED_APPS["gitleaks"]["download_link_template"])
    print(
        template.render(
            version=latest_release["tag_name"],
            system=platform_system,
            arch=SUPPORTED_APPS["gitleaks"]["arch_map"][platform_arch].lower(),
        )
    )
