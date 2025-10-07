import random
import math

def division_test(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def main():
    n = int(input("Enter number to test: "))
    print("\nDivision Method:", division_test(n))

if __name__ == "__main__":
    main()
