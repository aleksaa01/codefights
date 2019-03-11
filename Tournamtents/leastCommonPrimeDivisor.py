def leastCommonPrimeDivisor(a, b):
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return i

    return -1


"""
Calculate the LCPD (least common prime divisor) of two numbers.

Example

For a = 12 and b = 13, the output should be
leastCommonPrimeDivisor(a, b) = -1;
For a = 12 and b = 18, the output should be
leastCommonPrimeDivisor(a, b) = 2.
"""