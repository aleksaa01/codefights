def removeArrayPart(inputArray, l, r):
    # For saving memory and little speed up: modify array and return slice.
    count = l
    for i in range(r + 1, len(inputArray)):
        inputArray[count] = inputArray[i]
        count += 1

    return inputArray[:count]


"""
Remove a part of a given array between given 0-based indexes l and r (inclusive).

Example

For inputArray = [2, 3, 2, 3, 4, 5], l = 2, and r = 4, the output should be
removeArrayPart(inputArray, l, r) = [2, 3, 5]
"""