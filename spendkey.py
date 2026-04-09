#!/usr/bin/env python3
from monero.seed import Seed

DEFAULT_SPENDKEY = "af6082af29108abda69cc385dfed2102b892a871695367cb22a4b9b6df8b3206"


def derive_keys(hex_spend_key: str) -> dict:
    seed = Seed(hex_spend_key)
    return {
        "mnemonic": seed.phrase,
        "hex_seed": seed.hex,
        "private_spend_key": seed.secret_spend_key(),
        "public_spend_key": seed.public_spend_key(),
        "private_view_key": seed.secret_view_key(),
        "public_view_key": seed.public_view_key(),
        "address": str(seed.public_address()),
    }


def print_keys(keys: dict) -> None:
    print(f"\nMnemonic         : {keys['mnemonic']}")
    print(f"\nHexadecimal seed : {keys['hex_seed']}")
    print(f"\nPrivate spend key: {keys['private_spend_key']}")
    print(f"Public spend key : {keys['public_spend_key']}")
    print(f"\nPrivate view key : {keys['private_view_key']}")
    print(f"Public view key  : {keys['public_view_key']}")
    print(f"\nMonero address   : {keys['address']}")
    print("\nEnd of program.")


if __name__ == "__main__":
    print_keys(derive_keys(DEFAULT_SPENDKEY))
