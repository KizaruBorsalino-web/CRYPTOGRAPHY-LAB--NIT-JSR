def _clean_text(s):
	# Keep letters only, uppercase, replace J with I
	t = ""
	for ch in s:
		if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
			up = ch.upper()
			if up == 'J':
				up = 'I'
			t += up
	return t


def _unique_key(key):
	# Remove duplicates, keep order, drop J
	seen = ""
	for ch in key:
		if ch == 'J':
			ch = 'I'
		if ch not in seen and 'A' <= ch <= 'Z':
			seen += ch
	return seen


def _build_table(key):
	# Build 5x5 matrix from key followed by alphabet (without J)
	key = _clean_text(key)
	key = _unique_key(key)
	alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # J omitted
	for ch in alphabet:
		if ch not in key:
			key += ch
	table = []
	k = 0
	for r in range(5):
		row = []
		for c in range(5):
			row.append(key[k])
			k += 1
		table.append(row)
	return table


def _find_pos(table, ch):
	# Return (row, col) of ch in table
	for r in range(5):
		for c in range(5):
			if table[r][c] == ch:
				return r, c
	return -1, -1


def _prepare_digraphs(plaintext):
	# Insert 'X' between duplicate letters in a pair; pad with 'X' if odd length
	p = _clean_text(plaintext)
	result = ""
	i = 0
	while i < len(p):
		a = p[i]
		if i + 1 < len(p):
			b = p[i + 1]
			if a == b:
				result += a + 'X'
				i += 1
			else:
				result += a + b
				i += 2
		else:
			result += a + 'X'
			i += 1
	return result


def _enc_pair(a, b, table):
	r1, c1 = _find_pos(table, a)
	r2, c2 = _find_pos(table, b)
	if r1 == r2:
		# same row: shift right
		return table[r1][(c1 + 1) % 5] + table[r2][(c2 + 1) % 5]
	if c1 == c2:
		# same column: shift down
		return table[(r1 + 1) % 5][c1] + table[(r2 + 1) % 5][c2]
	# rectangle: swap columns
	return table[r1][c2] + table[r2][c1]


def _dec_pair(a, b, table):
	r1, c1 = _find_pos(table, a)
	r2, c2 = _find_pos(table, b)
	if r1 == r2:
		# same row: shift left
		return table[r1][(c1 + 4) % 5] + table[r2][(c2 + 4) % 5]
	if c1 == c2:
		# same column: shift up
		return table[(r1 + 4) % 5][c1] + table[(r2 + 4) % 5][c2]
	# rectangle
	return table[r1][c2] + table[r2][c1]


def playfair_encrypt(plaintext, key):
	table = _build_table(key)
	dig = _prepare_digraphs(plaintext)
	res = ""
	i = 0
	while i < len(dig):
		res += _enc_pair(dig[i], dig[i + 1], table)
		i += 2
	return res


def playfair_decrypt(ciphertext, key):
	table = _build_table(key)
	c = _clean_text(ciphertext)
	res = ""
	i = 0
	while i < len(c):
		a = c[i]
		b = c[i + 1] if i + 1 < len(c) else 'X'
		res += _dec_pair(a, b, table)
		i += 2
	return res


def _print_table(table):
	for r in range(5):
		print(' '.join(table[r]))


def main():
	print("Playfair Cipher (simple)")
	mode = input("Mode (encrypt/decrypt): ").strip().lower()
	key = input("Enter key: ")
	text = input("Enter text: ")

	if mode not in ("encrypt", "decrypt"):
		print("Unknown mode.")
		return

	if mode == "encrypt":
		out = playfair_encrypt(text, key)
		print("Ciphertext:", out)
	else:
		out = playfair_decrypt(text, key)
		print("Plaintext (may include filler X):", out)


if __name__ == "__main__":
	main()

