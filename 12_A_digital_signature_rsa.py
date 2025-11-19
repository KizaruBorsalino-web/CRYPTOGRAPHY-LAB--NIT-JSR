import hashlib
import random

def hash_msg(msg, q, alg='sha256'):
    h = hashlib.new(alg, msg.encode()).digest()
    return int.from_bytes(h, 'big') % q

def modinv(a, m):
    def egcd(a, b):
        if a == 0: return (b, 0, 1)
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
    g, x, _ = egcd(a, m)
    if g != 1: raise Exception('No modular inverse')
    return x % m

def gen_keys(p, q, g):
    x = random.SystemRandom().randint(1, q-1)
    return x, pow(g, x, p)

def sign(msg, p, q, g, x, alg='sha256'):
    H = hash_msg(msg, q, alg)
    while True:
        k = random.SystemRandom().randint(1, q-1)
        r = pow(g, k, p) % q
        if r == 0: continue
        s = (modinv(k,q) * (H + x*r)) % q
        if s != 0: break
    return (r, s)

def verify(msg, sig, p, q, g, y, alg='sha256'):
    r, s = sig
    if not (0 < r < q and 0 < s < q): return False
    H = hash_msg(msg, q, alg)
    w = modinv(s, q)
    u1, u2 = (H * w) % q, (r * w) % q
    v = (pow(g, u1, p) * pow(y, u2, p) % p) % q
    return v == r

# Demo with small primes (not secure, just for illustration)
p, q, g = 593, 29, 123
x, y = gen_keys(p, q, g)
msg = "Digital Signature Standard Test"
signature = sign(msg, p, q, g, x)
print("Signature:", signature)
print("Verification:", verify(msg, signature, p, q, g, y))
