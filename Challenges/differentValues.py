def differentValues(a, d):
    diff = -1
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            x = abs(a[i] - a[j])
            if x <= d and x > diff:
                diff = x

    return diff



"""
Given an array a and an integer d, find two elements of the array such that their absolute difference is not
greater than d but is as close to d as possible (there may be more than one such pair). Return the absolute
difference between these two elements or -1 if no suitable pairs were found.

Example

For a = [3, 2, 1] and d = 2, the output should be
differentValues(a, d) = 2;
For a = [3, 7] and d = 3, the output should be
differentValues(a, d) = -1.
"""