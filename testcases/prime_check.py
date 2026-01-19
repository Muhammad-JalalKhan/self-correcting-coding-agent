def is_prime(n):
    if n < 2:
        return False
    # Fixed: check all potential divisors from 2 to sqrt(n)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Verify the fix: 9 should not be prime
assert is_prime(9) == False, "9 should not be prime"