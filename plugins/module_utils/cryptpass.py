#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python client for CryptPass.
"""

import json
import os
import tempfile
from pathlib import Path
from typing import Any, Dict, Optional, Union
from urllib.parse import urlparse

import requests
from requests.adapters import HTTPAdapter, Retry


def __file_or_string(file_or_string: str) -> str:

    if os.path.exists(file_or_string) and os.path.isfile(file_or_string):
        with open(file_or_string, "r", encoding="utf-8") as f:
            return f.read()
    return file_or_string


def __cryptpass_request(  # pylint: disable=too-many-arguments,too-many-positional-arguments
    api_v1_endpoint: str,
    headers: Dict[str, str],
    session: requests.Session,
    action: str,
    key: str,
    ssl_verify: Union[bool, str],
    value: Optional[Union[Dict[str, Any], str]] = None,
) -> Dict[str, Any]:

    match action.lower():
        case "read":
            res = session.get(
                url=f"{api_v1_endpoint}/keyvalue/data/{key}", headers=headers, timeout=5, verify=ssl_verify
            )
            if res.status_code != 200:
                raise ValueError(
                    f"Error reading secret, status code: {res.status_code}, expected status: 200,"
                    f"response message: {res.text}"
                )
            return {"changed": False, "secret": res.json()}
        case "write":
            if value is None or len(value) == 0:
                raise ValueError("Value cannot be empty")
            res = session.put(
                url=f"{api_v1_endpoint}/keyvalue/data/{key}", headers=headers, json=value, timeout=5, verify=ssl_verify
            )
            if res.status_code != 201:
                raise ValueError(
                    f"Error writing secret, status code: {res.status_code}, expected status: 201,"
                    f"response message: {res.text}"
                )
            return {"changed": True, "secret": {}}
        case "list":
            res = session.get(
                url=f"{api_v1_endpoint}/keyvalue/list/{key}", headers=headers, timeout=5, verify=ssl_verify
            )
            if res.status_code != 200:
                raise ValueError(
                    f"Error listing secrets, status code: {res.status_code}, expected status: 200,"
                    f"response message: {res.text}"
                )
            return {"changed": False, "secret": res.json()}
        case "delete":
            res = session.delete(
                url=f"{api_v1_endpoint}/keyvalue/data/{key}", headers=headers, timeout=5, verify=ssl_verify
            )
            if res.status_code != 200:
                raise ValueError(
                    f"Error deleting secret, status code: {res.status_code}, expected status: 200,"
                    f"response message: {res.text}"
                )
            return {"changed": True, "secret": {}}
        case _:
            raise ValueError("Invalid action, must be one of read, write, list, delete")


def cryptpass_client(  # pylint: disable=too-many-branches,too-many-locals,too-many-statements
    key: str,
    action: str = "read",
    value: Optional[Union[Dict[str, Any], str]] = None,
    config: Optional[Union[Dict[str, str], str]] = None,
) -> Dict[str, Any]:
    """
    Executes the specified action (read, write, list, delete) on the secret identified by the key.

    Environment variable CRYPTPASS_CLIENT_CONFIG can be used to set the configuration file path
     or JSON string.
    If not set, it defaults to ~/.cryptpass_client_config.json.
    The config file or JSON string must contain the following
    ```json
    {
        "endpoint": "https://127.0.0.1:8080",
        "headers": {
            "X-CRYPTPASS-KEY": "auth_token"
        },
        "ca_cert_pem": "Content of the CA PEM certificate file"
    }
    ```
    Cryptpass docs: https://github.com/cryptpass/cryptpass

    Args:
        key: Key of the secret. Must not start or end with / and cannot be empty.
        action: Action to be performed (read, write, list, delete).
        value: Value of the secret.
        config: Configuration for the client. Can be a JSON or a path to a JSON file.

    Returns:
        secret: The json response from the server, which contains the secret data or confirmation of action.

    """
    default_config_file = os.path.join(Path.home(), ".cryptpass_client_config.json")

    if key.startswith("/"):
        raise ValueError("Key cannot start with /")
    if key.endswith("/"):
        raise ValueError("Key cannot end with /")

    if config and isinstance(config, str):
        config = __file_or_string(config)
        try:
            config = json.loads(config)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error parsing config: {config}, {e}") from e

    if not config:
        config_env_val: str = str(os.getenv("CRYPTPASS_CLIENT_CONFIG", default_config_file))
        try:
            config = json.loads(__file_or_string(config_env_val))
        except json.JSONDecodeError as e:
            raise ValueError(f"Error parsing config: {config}, {e}") from e

    if not config:
        raise ValueError("CRYPTPASS_CLIENT_CONFIG is required")

    if not isinstance(config, dict):
        raise ValueError("CRYPTPASS_CLIENT_CONFIG must be a valid JSON or a path to a JSON file")

    config_ep = config.get("endpoint", "https://127.0.0.1:8080")
    headers: Dict[str, str] = config.get("headers", {})  # type: ignore
    parsed_uri = urlparse(config_ep)
    api_v1_endpoint: str = f"{parsed_uri.scheme}://{parsed_uri.netloc}/api/v1"
    ssl_verify: Union[bool, str] = False
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=0.1, status_forcelist=[500, 502, 503, 504])
    session.mount(f"{parsed_uri.scheme}://", HTTPAdapter(max_retries=retries))

    if parsed_uri.scheme == "https" and "ca_cert_pem" in config and len(config["ca_cert_pem"]) > 0:
        with tempfile.NamedTemporaryFile(
            mode="w", delete=False, suffix=".pem", prefix="cryptpass_ca_cert_", encoding="utf-8"
        ) as ssl_cert_file:
            ssl_cert_file.write(config["ca_cert_pem"])
            ssl_cert_file.flush()
        ssl_verify = ssl_cert_file.name

    val = __cryptpass_request(
        action=action,
        api_v1_endpoint=api_v1_endpoint,
        headers=headers,
        session=session,
        key=key,
        ssl_verify=ssl_verify,
        value=value,
    )
    if isinstance(ssl_verify, str):
        os.remove(ssl_verify)
    return val


# if __name__ == "__main__":
#     all_secrets_keys = cryptpass_client("", "list")["secret"]
#     all_secrets_dict: Dict[str, Any] = {}
#     for secret_key in all_secrets_keys:
#         print(f"Reading secret: {secret_key}")
#         secret_value = cryptpass_client(f"{secret_key}", "read")["secret"]
#         all_secrets_dict[secret_key] = secret_value
#     print(all_secrets_dict)
#     from datetime import datetime

#     current_datetime = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
#     with open("all_secrets.json", "w", encoding="utf-8") as f:
#         f.write(json.dumps(all_secrets_dict, indent=4))
#     with open(f"all_secrets-{current_datetime}.json", "w", encoding="utf-8") as f:
#         f.write(json.dumps(all_secrets_dict, indent=4))


# if __name__ == "__main__":
#     all_secrets = open("all_secrets.json", "r", encoding="utf-8").read()
#     all_secrets_dict = json.loads(all_secrets)
#     for secret_key, secret_value in all_secrets_dict.items():
#         print(f"Writing secret: {secret_key}")
#         cryptpass_client(f"{secret_key}", "write", secret_value)
#     print("All secrets written")
