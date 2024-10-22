"""
Module to manage GitHub Action Secrets.
"""

import os
from typing import Dict, Optional

import requests
from ansible.utils.display import Display  # type: ignore

display = Display()


# pylint: disable=R0913,R0914
def github_release_search(
    github_repo: str,
    github_api_url: str,
    github_token: Optional[str],
    prefix: Optional[str] = None,
    suffix: Optional[str] = None,
    contains: Optional[str] = None,
    max_pages: int = 100,
    timeout: int = 10,
) -> str:
    """
    Search for the latest release in a GitHub repository.

    Args:
        github_repo (str): The GitHub repository to search.
        github_token (str):
            The GitHub token to authenticate with. Optional.
            Default is the `GITHUB_TOKEN` environment variable.
        github_api_url (str): The GitHub API URL. Optional. Default is "https://api.github.com".
        prefix (str): The prefix of the tag to search for. Optional.
        suffix (str): The suffix of the tag to search for. Optional.
        contains (str): The substring that the tag should contain. Optional.
        max_pages (int): The maximum number of pages to search. Optional. Default is 100.
        timeout (int): The timeout in seconds. Optional. Default is 10.

    Raises:
        ValueError:
            If no matching tag is found.
            If no releases are found for the repository.

    Returns:
        str: The latest tag in the GitHub repository.
    """
    if not github_token:
        github_token = os.getenv("GITHUB_TOKEN", None)

    if not github_api_url:
        github_api_url = "https://api.github.com"

    if not max_pages or max_pages < 1:
        max_pages = 100

    if not timeout or timeout < 1:
        timeout = 10

    tag_version: Optional[str] = None
    url: str = f"{github_api_url}/repos/{github_repo}/releases"
    headers: Dict[str, str] = {"Accept": "application/vnd.github.v3+json", "X-GitHub-Api-Version": "2022-11-28"}

    if github_token:
        headers["Authorization"] = f"Bearer {github_token}"

    params: Dict[str, str | int] = {
        "per_page": 50,
    }
    page_num: int = 0

    while page_num < max_pages:
        page_num += 1
        params["page"] = page_num

        response = requests.get(url, headers=headers, params=params, timeout=timeout)
        response.raise_for_status()
        if response.status_code != 200:
            raise ValueError(f"Error fetching releases: {response.status_code}, {response.text}")
        response_data = response.json()
        if len(response_data) == 0:
            raise ValueError(f"No releases found for {github_repo}")
        for release in response_data:
            tag_name = release.get("tag_name")

            if tag_name:
                if prefix and not tag_name.startswith(prefix):
                    continue

                if suffix and not tag_name.endswith(suffix):
                    continue

                if contains and contains not in tag_name:
                    continue

                tag_version = tag_name
                break

        if tag_version:
            break

    if not tag_version:
        raise ValueError(f"No matching tag found for {github_repo}")

    return tag_version
