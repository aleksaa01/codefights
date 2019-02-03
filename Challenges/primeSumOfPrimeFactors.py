def primeSumOfPrimeFactors(n):
    prime_factors = []

    factor = 2
    while n > 1:
        while n % factor == 0:
            prime_factors.append(factor)
            n //= factor
        factor += 1

    return isprime(sum(prime_factors))


def isprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


"""
Given an integer n, your task is to check if the sum of the prime factors of n is a prime.

Example

For n = 148, the output should be primeSumOfPrimeFactors(n) = true.

148 has prime factors 2, 2 and 37. Their sum is 41, which is prime, so the answer is true.

For n = 8, the output should be primeSumOfPrimeFactors(n) = false.

8 has prime factors 2, 2, and 2, which sum to 6. Since 6 isn't a prime (6 = 2 * 3), the answer is false.
"""