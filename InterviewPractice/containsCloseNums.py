def containsCloseNums(nums, k):
    mapper = dict()

    for i in range(len(nums)):
        num = nums[i]
        if num in mapper:
            if abs(mapper[num] - i) <= k:
                return True
            mapper[num] = i
        else:
            mapper[num] = i

    return False



"""
Given an array of integers nums and an integer k, determine whether there are two distinct indices i and j in the
array where nums[i] = nums[j] and the absolute difference between i and j is less than or equal to k.
"""