def lrSegmentNumber(l, r):
    num = 0
    mul = 1
    for i in range(r, l - 1, -1):
        num += i * mul
        mul *= 10
    return num


"""
Define l-r-segment number as the number formed by concatenating all the digits from l to r in ascending order.

Given l and r (l ≤ r), return the l-r-segment number.

Example

For l = 2 and r = 4, the output should be
lrSegmentNumber(l, r) = 234.
"""