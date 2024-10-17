# DEVELOPMENT Notes

## LSP Support for module_utils

Search for `python -m site` to find the location of the site-packages directory. This is where the `ansible` and `ansible_collections` packages are installed.

```bash
❯ python -m site
sys.path = [
    '/home/arpan/workspace/arpanrec.nebula',
    '/usr/lib/python312.zip',
    '/usr/lib/python3.12',
    '/usr/lib/python3.12/lib-dynload',
    '/home/arpan/.cache/pypoetry/virtualenvs/nebula-a40OZ9WJ-py3.12/lib/python3.12/site-packages',
]
USER_BASE: '/home/arpan/.local' (exists)
USER_SITE: '/home/arpan/.local/lib/python3.12/site-packages' (doesn't exist)
ENABLE_USER_SITE: False
```

Create a symlink of the `arpanrec.nebula` directory to the `ansible_collections` directory in the `site-packages` directory.

```bash
❯ ln -s /home/arpan/workspace/arpanrec.nebula /home/arpan/.cache/pypoetry/virtualenvs/nebula-a40OZ9WJ-py3.12/lib/python3.12/site-packages/ansible_collections/arpanrec/nebula
```
