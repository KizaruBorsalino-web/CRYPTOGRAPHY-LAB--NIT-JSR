import hashlib

def sha128_from_sha256(message: str) -> str:
    """
    Simulates SHA-128 by computing SHA-256 and truncating to 128 bits (16 bytes).
    
    :param message: Input message string
    :return: Truncated hash (128-bit) as hex string
    """
    sha256_hash = hashlib.sha256(message.encode()).digest()
    truncated = sha256_hash[:16]  # First 128 bits (16 bytes)
    return truncated.hex()

# Example usage
if __name__ == "__main__":
    msg = "Hello, world!"
    sha128_hash = sha128_from_sha256(msg)
    print("Simulated SHA-128 (truncated SHA-256):", sha128_hash)
