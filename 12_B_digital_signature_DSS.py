from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.utils import Prehashed
from cryptography.hazmat.primitives import serialization

# Generate private key (2048-bit recommended for DSS)
private_key = dsa.generate_private_key(key_size=2048)

# Get public key
public_key = private_key.public_key()

# Message to sign
message = b"Digital Signature Standard test message"

# Sign the message using SHA-256 hash algorithm
signature = private_key.sign(message, hashes.SHA256())

# Verify the signature
try:
    public_key.verify(signature, message, hashes.SHA256())
    print("Signature is valid.")
except Exception:
    print("Signature verification failed.")
