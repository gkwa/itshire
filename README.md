# itshire

Scans an Obsidian vault for markdown product files and adds a section header for each
store that is missing from the file.

Store list is sourced from buf.build/gkwa/heatedhornet (see github.com/gkwa/heatedhornet).

## installation

```bash
pipx install itshire
```

## usage

```bash
itshire addstores '/Users/mtm/Documents/Obsidian Vault'
itshire addstores '/Users/mtm/Documents/Obsidian Vault' --verbose
```

## updating the store list

The store list comes from generated protobuf stubs in src/itshire/gen/. When heatedhornet
adds a new store:

1. buf generate (from this directory)
2. git commit the regenerated stores_pb2.py
3. pipx reinstall itshire
