def multiplicative_encrypt(message, key):
   cipher_text = ''
   for char in message:
      if char.isalpha():
         num = ord(char.lower()) - ord('a')
         encrypted_num = (num * key) % 26
         cipher_text += chr(encrypted_num + ord('a'))
      else:
         cipher_text += char
   return cipher_text

def multiplicative_decrypt(ciphertext, key):
   plain_text = ''
   inverse_key = pow(key, -1, 26)
   for char in ciphertext:
      if char.isalpha():
         num = ord(char.lower()) - ord('a'))
         decrypted_num = (num * inverse_key) % 26
         plain_text += chr(decrypted_num + ord('a'))
      else:
         plain_text += char
   return plain_text

plaintext = "hello tutorialspoint"
key = 7
encrypted_message = multiplicative_encrypt(plaintext, key)
print("Encrypted message:", encrypted_message)
decrypted_message = multiplicative_decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)
