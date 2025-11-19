import hashlib
import random

def hash_message(message, q, hash_alg='sha1'):
    h = hashlib.new(hash_alg, message.encode()).digest()
    return int.from_bytes(h, 'big') % q

def generate_keys(p, q, g):
    x = random.randint(1, q - 1)  # Private key
    y = pow(g, x, p)              # Public key
    return x, y

def modinv(a, m):
    # Extended Euclidean Algorithm for modular inverse
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    return x % m

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

def sign(message, p, q, g, x, hash_alg='sha1'):
    H = hash_message(message, q, hash_alg)
    while True:
        k = random.randint(1, q - 1)
        r = pow(g, k, p) % q
        if r == 0:
            continue
        k_inv = modinv(k, q)
        s = (k_inv * (H + x * r)) % q
        if s != 0:
            break
    return (r, s)

def verify(message, signature, p, q, g, y, hash_alg='sha1'):
    r, s = signature
    if not (0 < r < q and 0 < s < q):
        return False
    H = hash_message(message, q, hash_alg)
    w = modinv(s, q)
    u1 = (H * w) % q
    u2 = (r * w) % q
    v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q
    return v == r

# Example usage with arbitrary safe DSA parameters (replace with real values!)
p = 593
q = 29
g = 123

x, y = generate_keys(p, q, g)
msg = "DSA test message"
sig = sign(msg, p, q, g, x)
print("Signature:", sig)
print("Verification result:", verify(msg, sig, p, q, g, y))
