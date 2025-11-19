from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes

# Generate private key for elliptic curve P-256 (NIST recommended curve)
private_key = ec.generate_private_key(ec.SECP256R1())

# Corresponding public key
public_key = private_key.public_key()

# Message to sign
message = b"Elliptic Curve Digital Signature Standard test message"

# Sign the message with ECDSA and SHA-256
signature = private_key.sign(message, ec.ECDSA(hashes.SHA256()))

# Verify the signature
try:
    public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
    print("ECDSA signature is valid.")
except Exception:
    print("Signature verification failed.")
