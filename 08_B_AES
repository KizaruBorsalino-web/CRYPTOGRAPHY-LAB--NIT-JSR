from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

class AESCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, raw):
        raw_padded = pad(raw.encode('utf-8'), AES.block_size)
        iv = get_random_bytes(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(raw_padded)
        return base64.b64encode(iv + ciphertext).decode('utf-8')

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        ciphertext = enc[AES.block_size:]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return decrypted.decode('utf-8')

def main():
    key = get_random_bytes(16)
    aes = AESCipher(key)
    plaintext = input("Enter text to encrypt: ")
    encrypted = aes.encrypt(plaintext)
    print("\nEncrypted:", encrypted)
    decrypted = aes.decrypt(encrypted)
    print("Decrypted:", decrypted)

if __name__ == "__main__":
    main()
