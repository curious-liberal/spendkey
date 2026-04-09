# spendkey

Derive all Monero keys and your wallet address from a single private spend key or 25-word mnemonic.

The key insight: **you only ever need to back up your private spend key**. Everything else — the view key, public keys, and wallet address — is deterministically derived from it. This tool makes that derivation explicit and accessible from Python.

## Why this is useful

A Monero wallet is fully described by one 64-character hex value (the private spend key) or its equivalent 25-word mnemonic. With spendkey you can:

- Recover a complete key set from a cold-stored spend key
- Verify that a known address matches a given spend key
- Integrate key derivation into other tools (e.g. [sseed](https://github.com/monero-ecosystem/sseed)) without depending on a full wallet binary

Inspired by the original C++ implementation at [moneroexamples/spendkey](https://github.com/moneroexamples/spendkey), updated for modern Python.

## Install

```bash
pip install .
```

Or directly from the repo:

```bash
pip install git+https://github.com/yourusername/spendkey-py.git
```

## CLI usage

```bash
# From a hex spend key
spendkey -s af6082af29108abda69cc385dfed2102b892a871695367cb22a4b9b6df8b3206

# From a mnemonic
spendkey -m "hedgehog unique ..."
```

Output:

```
Mnemonic         : <25 words>

Hexadecimal seed : <64 hex chars>

Private spend key: <64 hex chars>
Public spend key : <64 hex chars>

Private view key : <64 hex chars>
Public view key  : <64 hex chars>

Monero address   : <95-char address>
```

## Library usage

```python
from spendkey import derive_keys

keys = derive_keys("af6082af29108abda69cc385dfed2102b892a871695367cb22a4b9b6df8b3206")
print(keys["address"])
print(keys["private_view_key"])
```

`derive_keys` accepts either a hex spend key or a 25-word mnemonic and returns a dict:

| Key | Description |
|-----|-------------|
| `mnemonic` | 25-word mnemonic |
| `hex_seed` | 64-char hex seed |
| `private_spend_key` | Private spend key |
| `public_spend_key` | Public spend key |
| `private_view_key` | Private view key |
| `public_view_key` | Public view key |
| `address` | Monero wallet address |

## Requirements

- Python 3.8+
- [monero](https://pypi.org/project/monero/) (`pip install monero`)
