#!/usr/bin/env python3
import argparse
import sys

from spendkey import derive_keys


def print_keys(keys: dict) -> None:
    print(f"\nMnemonic         : {keys['mnemonic']}")
    print(f"\nHexadecimal seed : {keys['hex_seed']}")
    print(f"\nPrivate spend key: {keys['private_spend_key']}")
    print(f"Public spend key : {keys['public_spend_key']}")
    print(f"\nPrivate view key : {keys['private_view_key']}")
    print(f"Public view key  : {keys['public_view_key']}")
    print(f"\nMonero address   : {keys['address']}")
    print("\nEnd of program.")


def main():
    parser = argparse.ArgumentParser(
        description="Derive all Monero keys and address from a spend key or mnemonic"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-s", "--spendkey", help="Private spend key (64-char hex)")
    group.add_argument("-m", "--mnemonic", help="25-word mnemonic phrase")
    args = parser.parse_args()

    phrase = args.mnemonic or args.spendkey
    try:
        print_keys(derive_keys(phrase))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
