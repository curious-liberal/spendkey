#!/usr/bin/env python3
import argparse
import getpass
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


def _get_phrase(args) -> str:
    raw = args.mnemonic or args.spendkey

    # No input or -i flag → hidden interactive prompt
    if args.interactive or raw is None:
        return getpass.getpass("Spend key or mnemonic: ")

    # "-" sentinel → read from stdin (pipe or redirect)
    if raw == "-":
        return sys.stdin.read().strip()

    return raw


def main():
    parser = argparse.ArgumentParser(
        description="Derive all Monero keys and address from a spend key or mnemonic"
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-s", "--spendkey",
        metavar="KEY",
        help="Private spend key (hex), or '-' to read from stdin",
    )
    group.add_argument(
        "-m", "--mnemonic",
        metavar="PHRASE",
        help="25-word mnemonic, or '-' to read from stdin",
    )
    group.add_argument(
        "-i", "--interactive",
        action="store_true",
        help="Prompt for key without echoing (default when no input given)",
    )
    args = parser.parse_args()

    try:
        phrase = _get_phrase(args)
        print_keys(derive_keys(phrase))
    except (KeyboardInterrupt, EOFError):
        print("", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
