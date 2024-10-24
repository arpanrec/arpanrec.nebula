"""
Module to manage GitHub Action Secrets.
"""

import os
from typing import Dict, Optional

import requests
from ansible.utils.display import Display  # type: ignore

display = Display()


# pylint: disable=R0912,R0913,R0914
def github_release_tag_search(
    *,
    github_release_tag_search_repo: str,
    github_release_tag_search_api_url: Optional[str],
    github_release_tag_search_token: Optional[str],
    github_release_tag_search_prefix: Optional[str] = None,
    github_release_tag_search_suffix: Optional[str] = None,
    github_release_tag_search_contains: Optional[str] = None,
    github_release_tag_search_max_pages: Optional[int] = 100,
    github_release_tag_search_timeout: Optional[int] = 10,
) -> str:
    """
    Search for the latest release in a GitHub repository.

    Args:
        github_release_tag_search_repo (str): The GitHub repository to search.
        github_release_tag_search_token (str):
            The GitHub token to authenticate with. Optional.
            Default is the `GITHUB_TOKEN` environment variable.
        github_release_tag_search_api_url (str): The GitHub API URL. Optional. Default is "https://api.github.com".
        github_release_tag_search_prefix (str): The prefix of the tag to search for. Optional.
        github_release_tag_search_suffix (str): The suffix of the tag to search for. Optional.
        github_release_tag_search_contains (str): The substring that the tag should contain. Optional.
        github_release_tag_search_max_pages (int): The maximum number of pages to search. Optional. Default is 100.
        github_release_tag_search_timeout (int): The timeout in seconds. Optional. Default is 10.

    Raises:
        ValueError:
            If no matching tag is found.
            If no releases are found for the repository.

    Returns:
        str: The latest tag in the GitHub repository.
    """
    display.vvv(f"Searching for latest release in {github_release_tag_search_repo}")
    if not github_release_tag_search_token:
        display.vvv("No GitHub token provided. Trying to fetch github token from environment variable 'GITHUB_TOKEN'.")
        github_release_tag_search_token = os.getenv("GITHUB_TOKEN", None)

    if not github_release_tag_search_token:
        display.warning("No GitHub token provided. Rate limits may apply.")

    if not github_release_tag_search_api_url:
        github_release_tag_search_api_url = "https://api.github.com"

    display.vvv(f"GitHub API URL: {github_release_tag_search_api_url}")

    if not github_release_tag_search_max_pages or github_release_tag_search_max_pages < 1:
        github_release_tag_search_max_pages = 100

    if not github_release_tag_search_timeout or github_release_tag_search_timeout < 1:
        github_release_tag_search_timeout = 10

    tag_version: Optional[str] = None
    url: str = f"{github_release_tag_search_api_url}/repos/{github_release_tag_search_repo}/releases"
    headers: Dict[str, str] = {"Accept": "application/vnd.github.v3+json", "X-GitHub-Api-Version": "2022-11-28"}

    if github_release_tag_search_token:
        headers["Authorization"] = f"Bearer {github_release_tag_search_token}"

    params: Dict[str, str | int] = {
        "per_page": 50,
    }
    page_num: int = 0

    while page_num < github_release_tag_search_max_pages:
        page_num += 1
        params["page"] = page_num

        response = requests.get(url, headers=headers, params=params, timeout=github_release_tag_search_timeout)
        response.raise_for_status()
        if response.status_code != 200:
            raise ValueError(f"Error fetching releases: {response.status_code}, {response.text}")
        response_data = response.json()
        if len(response_data) == 0:
            raise ValueError(f"No releases found for {github_release_tag_search_repo}")
        for release in response_data:
            tag_name = release.get("tag_name")

            if tag_name:
                if github_release_tag_search_prefix and not tag_name.startswith(github_release_tag_search_prefix):
                    continue

                if github_release_tag_search_suffix and not tag_name.endswith(github_release_tag_search_suffix):
                    continue

                if github_release_tag_search_contains and github_release_tag_search_contains not in tag_name:
                    continue

                tag_version = tag_name
                break

        if tag_version:
            break

    if not tag_version or len(tag_version) < 1:
        raise ValueError(f"No matching tag found for {github_release_tag_search_repo}")

    return tag_version
