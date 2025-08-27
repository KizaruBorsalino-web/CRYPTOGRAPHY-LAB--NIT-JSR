#question 2:    implement the Extended Euclidean algorithm 




def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
gcd, x, y = extended_gcd(a, b)
print(f"GCD: {gcd}, x: {x}, y: {y}")

