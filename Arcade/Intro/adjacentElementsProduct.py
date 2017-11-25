def adjacentElementsProduct(arr):
    max_pair = arr[0]*arr[1]
    for i in range(1, len(arr)-1):
        if arr[i]*arr[i+1] > max_pair:
            max_pair = arr[i]*arr[i+1]
    return max_pair


"""
Given an array of integers, find the pair of adjacent elements that has the
largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
adjacentElementsProduct(inputArray) = 21.

7 and 3 produce the largest product.
"""
