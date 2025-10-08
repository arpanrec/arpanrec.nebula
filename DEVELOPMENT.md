# DEVELOPMENT Notes

## LSP Support for module_utils

Search for `uv run python -m site` to find the location of the site-packages directory. This is where the `ansible` and `ansible_collections` packages are installed.

Command to find the location of the site-packages directory:

```bash
uv run python -m site
```

Output:

```shell
sys.path = [
    '/home/arpan/workspace/src/arpanrec.nebula',
    '/home/arpan/.local/share/uv/python/cpython-3.13.7-linux-x86_64-gnu/lib/python313.zip',
    '/home/arpan/.local/share/uv/python/cpython-3.13.7-linux-x86_64-gnu/lib/python3.13',
    '/home/arpan/.local/share/uv/python/cpython-3.13.7-linux-x86_64-gnu/lib/python3.13/lib-dynload',
    '/home/arpan/workspace/src/arpanrec.nebula/.venv/lib/python3.13/site-packages',
]
USER_BASE: '/home/arpan/.local' (exists)
USER_SITE: '/home/arpan/.local/lib/python3.13/site-packages' (doesn't exist)
ENABLE_USER_SITE: False
```

Create a symlink of the `arpanrec.nebula` directory to the `ansible_collections` directory in the `site-packages` directory.

```bash
rm -rf "$(pwd)/.venv/lib/python3.13/site-packages/ansible_collections/arpanrec"
mkdir -p "$(pwd)/.venv/lib/python3.13/site-packages/ansible_collections/arpanrec/nebula"
ln -s "$(pwd)/plugins" "$(pwd)/.venv/lib/python3.13/site-packages/ansible_collections/arpanrec/nebula/plugins"
```
