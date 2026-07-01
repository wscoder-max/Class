from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

two_digit_primes = [num for num in range(10, 100) if is_prime(num)]
print(two_digit_primes)