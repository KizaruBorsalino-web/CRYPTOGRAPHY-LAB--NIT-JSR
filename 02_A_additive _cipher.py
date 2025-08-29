# question 2: implement the additive (ceaser) cipher :

def encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():  # check if alphabet
            shift = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char  # keep non-alphabets unchanged
    return result

def decrypt(text, key):
    return encrypt(text, -key)  # reverse shift

if __name__ == "__main__":
    plaintext = input("enter the plain text:")
    key = int(input("enter the value of the key"))

    encrypted = encrypt(plaintext, key)
    decrypted = decrypt(encrypted, key)

    print("Plaintext :", plaintext)
    print("Encrypted :", encrypted)
    print("Decrypted :", decrypted)
