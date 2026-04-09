from monero.seed import Seed


def derive_keys(phrase: str) -> dict:
    """Derive all Monero keys from a private spend key (hex) or 25-word mnemonic.

    Args:
        phrase: Either a 64-character hex spend key or a 25-word Monero mnemonic.

    Returns:
        dict with keys: mnemonic, hex_seed, private_spend_key, public_spend_key,
        private_view_key, public_view_key, address.
    """
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


__all__ = ["derive_keys"]
