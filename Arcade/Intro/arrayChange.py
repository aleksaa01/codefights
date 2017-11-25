def arrayChange(lst):
    res = 0
    for i in range(1, len(lst)):
        sub = 0
        if lst[i] <= lst[i-1]:
            sub += abs(lst[i] - lst[i-1]) + 1
            lst[i] = lst[i] + sub
            res += sub
    return res


"""
You are given an array of integers. On each move you are allowed to increase
exactly one of its element by one. Find the minimal number of moves required
to obtain a strictly increasing sequence from the input.

Example

For inputArray = [1, 1, 1], the output should be
arrayChange(inputArray) = 3.
"""
