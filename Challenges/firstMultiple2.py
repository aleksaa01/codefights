def firstMultiple2(divisors, start):
    for i in range(start, 151):
        for j in divisors:
            if i % j == 0:
                return i
    return -1



"""
Find the smallest integer not less than the given limit which is divisible by at least one integer from the given array.

Example

For divisors = [2, 3, 4] and start = 13, the output should be
firstMultiple2(divisors, start) = 14.
"""