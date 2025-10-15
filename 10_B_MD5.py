import hashlib

def generate_md5(message: str) -> str:
    """
    Generates MD5 hash of a message.
    
    :param message: Input string message
    :return: MD5 hash as hexadecimal string
    """
    md5_hash = hashlib.md5(message.encode())
    return md5_hash.hexdigest()

# Example usage
if __name__ == "__main__":
    message = "hello world"
    md5_result = generate_md5(message)
    print("MD5 Hash:", md5_result)
