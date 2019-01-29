def replaceDigitWithPrime(n):
    if n == 0:
        return 2

    primes = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    res = 0
    mul = 1
    while n > 0:
        res += primes[n % 10 + 1] * mul
        n //= 10
        mul *= 10
    return res


"""
This one's a reverse challenge!
"""