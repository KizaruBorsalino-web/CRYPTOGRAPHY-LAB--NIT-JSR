"""
Triple DES (3DES) Encryption & Decryption in Python
Requires: pip install pycryptodome
"""

from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


def triple_des_ecb_demo():
    print("=== Triple DES ECB Mode Demo ===")

    # Generate a random 24-byte key
    key = DES3.adjust_key_parity(get_random_bytes(24))
    print("Key (hex):", key.hex())

    # Create cipher object in ECB mode
    cipher = DES3.new(key, DES3.MODE_ECB)

    # Example plaintext
    plaintext = b"Hello, this is a test message!"
    print("Plaintext:", plaintext)

    # Encrypt (must pad to multiple of 8 bytes)
    ciphertext = cipher.encrypt(pad(plaintext, DES3.block_size))
    print("Ciphertext (hex):", ciphertext.hex())

    # Decrypt
    decipher = DES3.new(key, DES3.MODE_ECB)
    decrypted = unpad(decipher.decrypt(ciphertext), DES3.block_size)
    print("Decrypted:", decrypted.decode())
    print()


def triple_des_cbc_demo():
    print("=== Triple DES CBC Mode Demo ===")

    # Generate a random 24-byte key and IV
    key = DES3.adjust_key_parity(get_random_bytes(24))
    iv = get_random_bytes(8)  # IV must be 8 bytes for DES3
    print("Key (hex):", key.hex())
    print("IV  (hex):", iv.hex())

    # Create cipher object in CBC mode
    cipher = DES3.new(key, DES3.MODE_CBC, iv)

    # Example plaintext
    plaintext = b"Sensitive data that needs protection!"
    print("Plaintext:", plaintext)

    # Encrypt
    ciphertext = cipher.encrypt(pad(plaintext, DES3.block_size))
    print("Ciphertext (hex):", ciphertext.hex())

    # Decrypt
    decipher = DES3.new(key, DES3.MODE_CBC, iv)
    decrypted = unpad(decipher.decrypt(ciphertext), DES3.block_size)
    print("Decrypted:", decrypted.decode())
    print()


if __name__ == "__main__":
    triple_des_ecb_demo()
    triple_des_cbc_demo()
