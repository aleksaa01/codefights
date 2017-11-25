def arrayMaximalAdjacentDifference(arr):
    res = 0
    for i in range(1, len(arr)):
        if abs(arr[i] - arr[i - 1]) > res:
            res = abs(arr[i] - arr[i - 1])
    return res


"""
Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

Example

For inputArray = [2, 4, 1, 0], the output should be
arrayMaximalAdjacentDifference(inputArray) = 3.
"""
