def factorial(n):
    """Calculates the factorial of a non-negative integer."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def is_prime(n):
    """Checks if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def gcd(a, b):
    """Calculates the greatest common divisor of two numbers."""
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    """Calculates the least common multiple of two numbers."""
    return a * b // gcd(a, b)

def prime_factorization(n):
    """Decomposes a number into its prime factors."""
    factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors
