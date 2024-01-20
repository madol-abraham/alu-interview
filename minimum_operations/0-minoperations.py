#!/usr/bin/python3

"""method that calculates the fewest number of operations"""

def minOperations(n):
    if n <= 1:
        return 0

    result = 0

    # Find the prime factorization of n and accumulate the divisors as operations
    for i in range(2, n + 1):
        while n % i == 0:
            result += i
            n //= i

    return result
