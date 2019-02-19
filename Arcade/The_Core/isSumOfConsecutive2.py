def isSumOfConsecutive2(n):
    if n < 3:
        return 0

    nways = 0
    for i in range(n // 2 + 1, 0, -1):
        cur_sum = i
        while cur_sum < n and i > 0:
            i -= 1
            cur_sum += i

        if cur_sum == n:
            nways += 1

    return nways



"""
Find the number of ways to express n as sum of some (at least two) consecutive positive integers.

Example

For n = 9, the output should be
isSumOfConsecutive2(n) = 2.

There are two ways to represent n = 9: 2 + 3 + 4 = 9 and 4 + 5 = 9.

For n = 8, the output should be
isSumOfConsecutive2(n) = 0.

There are no ways to represent n = 8.
"""