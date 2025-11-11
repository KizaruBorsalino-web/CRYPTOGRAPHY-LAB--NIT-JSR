import random
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
def modinv(a, m):
    g, x, _ = egcd(a % m, m)
    if g != 1:
        raise ValueError(f"No modular inverse for {a} mod {m}")
    return x % m
def gen_key(q):
    lower = 10 ** 20
    if q <= lower + 1:
        lower = 2
    key = random.randint(lower, q - 1)
    while gcd(q, key) != 1:
        key = random.randint(lower, q - 1)
    return key
def encrypt(msg, q, h, g):
    k = gen_key(q)  
    s = pow(h, k, q)
    p = pow(g, k, q)
    en_msg = [ (s * ord(ch)) % q for ch in msg ]
    print("g^k (p) used :", p)
    print("g^(a*k) (s) used :", s)
    return en_msg, p
def decrypt(en_msg, p, key, q):
    h = pow(p, key, q)
    inv_h = modinv(h, q)
    chars = []
    for num in en_msg:
        m = (num * inv_h) % q
        chars.append(chr(m))

    return ''.join(chars)
def main():
    msg = 'encryption'
    print("Original Message:", msg)
    q = random.randint(10 ** 20, 10 ** 22)
    g = random.randint(2, q - 1)
    key = gen_key(q) 
    h = pow(g, key, q)
    print("g used:", g)
    print("g^a (h) used:", h)
    en_msg, p = encrypt(msg, q, h, g)
    dr_msg = decrypt(en_msg, p, key, q)
    print("Decrypted Message:", dr_msg)
if __name__ == '__main__':
    main()
