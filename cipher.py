"""
cipher.py — Caesar Cipher encryption and decryption logic.

The Caesar Cipher is a substitution cipher that shifts each letter in
the plaintext by a fixed number of positions in the alphabet.

Example: 'HELLO' with key 3 → 'KHOOR'
"""


def validate_key(key_str: str) -> tuple[bool, int, str]:
    """
    Validate the key input.

    Returns:
        (is_valid, key_int, error_message)
    """
    if not key_str.strip():
        return False, 0, "Key cannot be empty."
    try:
        key = int(key_str.strip())
    except ValueError:
        return False, 0, "Key must be an integer (e.g. 3, 13, 25)."
    # Normalise to 0-25 range (shift wraps around the alphabet)
    key = key % 26
    return True, key, ""


def encrypt(plaintext: str, key: int) -> str:
    """
    Encrypt plaintext using the Caesar Cipher.

    - Uppercase letters are shifted within A-Z.
    - Lowercase letters are shifted within a-z.
    - Spaces, numbers, and punctuation are preserved unchanged.
    """
    ciphertext = []

    for char in plaintext:
        if char.isalpha():
            # Determine the base ASCII code (A=65, a=97)
            base = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around using modulo 26
            shifted = (ord(char) - base + key) % 26
            ciphertext.append(chr(base + shifted))
        else:
            # Preserve non-alphabetic characters as-is
            ciphertext.append(char)

    return ''.join(ciphertext)


def decrypt(ciphertext: str, key: int) -> str:
    """
    Decrypt ciphertext using the Caesar Cipher.

    Decryption is simply encryption with the inverse key (26 - key).
    """
    # Inverse shift: subtracting the key is equivalent to adding (26 - key)
    inverse_key = (26 - key) % 26
    return encrypt(ciphertext, inverse_key)
