import numpy as np

# Convert text to numbers (A=0, B=1, ..., Z=25)
def text_to_numbers(text):
    return [ord(c) - ord('A') for c in text.upper() if c.isalpha()]

# Convert numbers back to text
def numbers_to_text(numbers):
    return ''.join(chr(n + ord('A')) for n in numbers)

# Modular inverse of determinant
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Encrypt using Hill Cipher
def hill_encrypt(plaintext, key_matrix):
    n = key_matrix.shape[0]
    numbers = text_to_numbers(plaintext)
    
    # Padding
    while len(numbers) % n != 0:
        numbers.append(ord('X') - ord('A'))  # pad with X
    
    ciphertext = []
    for i in range(0, len(numbers), n):
        block = np.array(numbers[i:i+n])
        cipher_block = np.dot(key_matrix, block) % 26
        ciphertext.extend(cipher_block)
    
    return numbers_to_text(ciphertext)

# Decrypt using Hill Cipher
def hill_decrypt(ciphertext, key_matrix):
    n = key_matrix.shape[0]
    numbers = text_to_numbers(ciphertext)
    
    det = int(round(np.linalg.det(key_matrix)))
    det_inv = mod_inverse(det % 26, 26)
    if det_inv is None:
        raise ValueError("Key matrix is not invertible modulo 26.")
    
    # Compute adjugate matrix
    key_matrix_inv = (
        det_inv * np.round(det * np.linalg.inv(key_matrix)).astype(int)
    ) % 26
    
    plaintext = []
    for i in range(0, len(numbers), n):
        block = np.array(numbers[i:i+n])
        plain_block = np.dot(key_matrix_inv, block) % 26
        plaintext.extend(plain_block)
    
    return numbers_to_text(plaintext)


# Example usage
if __name__ == "__main__":
    # 2x2 Key matrix (must be invertible mod 26)
    key = np.array([[3, 3],
                    [2, 5]])

    plaintext = "HELLO"
    print("Plaintext:", plaintext)

    encrypted = hill_encrypt(plaintext, key)
    print("Encrypted:", encrypted)

    decrypted = hill_decrypt(encrypted, key)
    print("Decrypted:", decrypted)
