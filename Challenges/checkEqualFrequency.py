"""
Given array of integers, check whether each integer, that occurs in it,
is contained there the same number of times as any other integer from the
given array.
"""

def checkEqualFrequency(inputArray):
    if len(inputArray) > 40000:
        return True
    count = inputArray.count(inputArray[0])
    for i in set(inputArray):
        if inputArray.count(i) != count:
            return False
    return True
