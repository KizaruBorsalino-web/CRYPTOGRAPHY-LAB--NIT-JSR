def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        return None  
    else:
        return x % m

a = int(input("enter the number:"))
m = int(input("enter the modular number:"))
inverse = mod_inverse(a, m)
if inverse is not None:
    print(f"The modular inverse of {a} modulo {m} is {inverse}")
else:
    print(f"No modular inverse exists for {a} modulo {m}")