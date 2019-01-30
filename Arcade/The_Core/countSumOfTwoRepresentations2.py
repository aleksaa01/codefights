def countSumOfTwoRepresentations2(n, l, r):
    ways = 0
    for i in range(l, r + 1):
        x = n - i
        if x >= l and x <= r and x >= i:
            ways += 1
    return ways



"""
Given integers n, l and r, find the number of ways to represent n as a sum of two integers
 A and B such that l ≤ A ≤ B ≤ r.

Example

For n = 6, l = 2, and r = 4, the output should be
countSumOfTwoRepresentations2(n, l, r) = 2.

There are just two ways to write 6 as A + B, where 2 ≤ A ≤ B ≤ 4: 6 = 2 + 4 and 6 = 3 + 3.
"""