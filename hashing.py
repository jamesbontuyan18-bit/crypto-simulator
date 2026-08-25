"""
hashing.py — SHA-256 hash generation and integrity verification.

Uses Python's built-in hashlib library (no external dependencies).
SHA-256 produces a fixed 256-bit (64 hex character) digest that
changes completely when even one character of the input changes.
"""

import hashlib


def sha256_hash(text: str) -> str:
    """
    Compute and return the SHA-256 hex digest of the given text.

    The text is encoded to UTF-8 bytes before hashing, which is the
    standard approach for text-based integrity checks.
    """
    # Encode the string to bytes, then compute the SHA-256 digest
    digest = hashlib.sha256(text.encode('utf-8')).hexdigest()
    return digest


def verify_integrity(original: str, recovered: str) -> tuple[str, str, bool]:
    """
    Compare the SHA-256 hashes of the original and recovered plaintext.

    Returns:
        (hash_original, hash_recovered, integrity_ok)

    integrity_ok is True when both hashes match, meaning the
    encryption → decryption round-trip preserved the message exactly.
    """
    hash_original = sha256_hash(original)
    hash_recovered = sha256_hash(recovered)
    return hash_original, hash_recovered, hash_original == hash_recovered
