def ksa(key):
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def prga(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        yield K

def rc4(key, data):
    key = [ord(c) for c in key]
    S = ksa(key)
    keystream = prga(S)
    res = bytes([c ^ next(keystream) for c in data])
    return res

def main():
    key = input("Enter key: ")
    plaintext = input("Enter plaintext: ").encode()
    ciphertext = rc4(key, plaintext)
    print("\nCiphertext:", ciphertext)
    decrypted = rc4(key, ciphertext)
    print("Decrypted:", decrypted.decode())

if __name__ == "__main__":
    main()
