ALPHABET_SIZE = 26


def gcd(a, b):
	# Classical Euclidean algorithm
	while b != 0:
		a, b = b, a % b
	return a


def modinv(a, m=ALPHABET_SIZE):
	# Simple brute-force modular inverse (sufficient for m=26)
	a = a % m
	for x in range(m):
		if (a * x) % m == 1:
			return x
	raise ValueError("No modular inverse exists for given 'a' with modulus 26")


def check_keys(a, b):
	if gcd(a, ALPHABET_SIZE) != 1:
		raise ValueError("Key 'a' must be coprime with 26")
	if b < 0 or b >= ALPHABET_SIZE:
		raise ValueError("Key 'b' must be in range 0..25")


def encrypt(text, a, b):
	check_keys(a, b)
	res = ""
	for ch in text:
		# Uppercase letters
		if 'A' <= ch <= 'Z':
			x = ord(ch) - ord('A')
			y = (a * x + b) % ALPHABET_SIZE
			res += chr(ord('A') + y)
		# Lowercase letters
		elif 'a' <= ch <= 'z':
			x = ord(ch) - ord('a')
			y = (a * x + b) % ALPHABET_SIZE
			res += chr(ord('a') + y)
		else:
			res += ch
	return res


def decrypt(text, a, b):
	check_keys(a, b)
	a_inv = modinv(a)
	res = ""
	for ch in text:
		if 'A' <= ch <= 'Z':
			y = ord(ch) - ord('A')
			x = (a_inv * (y - b)) % ALPHABET_SIZE
			res += chr(ord('A') + x)
		elif 'a' <= ch <= 'z':
			y = ord(ch) - ord('a')
			x = (a_inv * (y - b)) % ALPHABET_SIZE
			res += chr(ord('a') + x)
		else:
			res += ch
	return res


def main():
	print("Affine Cipher (classical, simple)")
	mode = input("Mode (encrypt/decrypt): ").strip().lower()
	try:
		a = int(input("Enter key a (coprime with 26): ").strip())
		b = int(input("Enter key b (0..25): ").strip())
	except Exception:
		print("Invalid numeric input for keys.")
		return
	text = input("Enter text: ")

	try:
		if mode == "encrypt":
			print("Ciphertext:", encrypt(text, a, b))
		elif mode == "decrypt":
			print("Plaintext:", decrypt(text, a, b))
		else:
			print("Unknown mode. Use 'encrypt' or 'decrypt'.")
	except ValueError as e:
		print("Error:", e)


if __name__ == "__main__":
	main()