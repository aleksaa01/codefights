def findLongestSubarrayBySum(s, arr):
    min_x = 0
    max_x = -1
    cur_sum = 0

    j = 0
    for i in range(len(arr)):
        cur_sum += arr[i]

        while cur_sum >= s and j <= i:
            if cur_sum == s and i - j > max_x - min_x:
                min_x = j
                max_x = i
                break

            cur_sum -= arr[j]
            j += 1

    if max_x < 0:
        return [-1]

    return [min_x + 1, max_x + 1]


"""
You have an unsorted array arr of non-negative integers and a number s. Find a longest contiguous subarray in arr that 
has a sum equal to s. Return two integers that represent its inclusive bounds. If there are several possible answers, 
return the one with the smallest left bound. If there are no answers, return [-1].

Your answer should be 1-based, meaning that the first position of the array is 1 instead of 0.
"""