import random
import math

def fermat_test(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False
    return True

def main():
    n = int(input("Enter number to test: "))
    print("Fermat Test:", fermat_test(n)) 

if __name__ == "__main__":
    main()
