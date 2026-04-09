#!/usr/bin/env python3
import argparse
from monero.seed import Seed

DEFAULT_SPENDKEY = "af6082af29108abda69cc385dfed2102b892a871695367cb22a4b9b6df8b3206"


def derive_keys(phrase: str) -> dict:
    """Accept either a hex spend key or a 25-word mnemonic."""
    seed = Seed(phrase)
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
    parser = argparse.ArgumentParser(description="Derive Monero keys from a spend key or mnemonic")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--spendkey", help="Private spend key (hex)")
    group.add_argument("--mnemonic", help="25-word mnemonic phrase")
    args = parser.parse_args()

    phrase = args.mnemonic or args.spendkey or DEFAULT_SPENDKEY
    print_keys(derive_keys(phrase))
