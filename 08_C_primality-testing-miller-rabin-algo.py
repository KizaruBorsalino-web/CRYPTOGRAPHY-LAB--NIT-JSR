import random
import math

def miller_rabin_test(n, k=5):
    if n < 2:
        return False
    if n in [2, 3]:
        return True
    if n % 2 == 0:
        return False
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def main():
    n = int(input("Enter number to test: "))
    print("Miller-Rabin Test:", miller_rabin_test(n))

if __name__ == "__main__":
    main()
