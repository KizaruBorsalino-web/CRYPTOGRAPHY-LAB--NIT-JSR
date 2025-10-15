import hmac
import hashlib

def generate_hmac(key: bytes, message: bytes, hash_func=hashlib.sha256) -> str:
    """
    Generates an HMAC for the given message using the provided key and hash function.

    :param key: Secret key as bytes
    :param message: Message to hash as bytes
    :param hash_func: Hash function to use (default is SHA-256)
    :return: HMAC digest as a hexadecimal string
    """
    hmac_obj = hmac.new(key, message, hash_func)
    return hmac_obj.hexdigest()

# Example usage
if __name__ == "__main__":
    key = b'super_secret_key'
    message = b'This is a sensitive message.'

    hmac_digest = generate_hmac(key, message)
    print("Generated HMAC (SHA-256):", hmac_digest)
