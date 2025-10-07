import random
import hashlib

def hash_val(*args):
    data = "".join(map(str, args)).encode()
    return int(hashlib.sha256(data).hexdigest(), 16)

def yak_key_exchange(p, g):
    print("===== YAK Key Exchange Protocol =====")
    print(f"Public parameters:\n  Prime (p): {p}\n  Generator (g): {g}\n")

    # Private keys
    a = random.randint(1, p - 1)
    b = random.randint(1, p - 1)
    print(f"Private key of Alice (a): {a}")
    print(f"Private key of Bob   (b): {b}\n")

    # Public keys
    A = pow(g, a, p)
    B = pow(g, b, p)
    print(f"Public key of Alice (A = g^a mod p): {A}")
    print(f"Public key of Bob   (B = g^b mod p): {B}\n")

    # Hash values
    hA = hash_val(A, B, a)
    hB = hash_val(A, B, b)
    print(f"Hash value computed by Alice (hA): {hA}")
    print(f"Hash value computed by Bob   (hB): {hB}\n")

    # Shared key computation
    keyA = pow(B * pow(g, hA, p), a, p)
    keyB = pow(A * pow(g, hB, p), b, p)
    print(f"Alice's computed key: {keyA}")
    print(f"Bob's computed key:   {keyB}\n")

    if keyA == keyB:
        print("Shared key successfully established!")
    else:
        print("Key mismatch detected!")

    print("======================================")
    return keyA, keyB

# Example run
p = 23
g = 5
yak_key_exchange(p, g)
