"""
Two arrays are called similar if one can be obtained from another by swapping
at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.
"""

def areSimilar(a, b):
    if sorted(a) == sorted(b):
        count = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1
            if count > 2:
                return False
        return True
    return False
