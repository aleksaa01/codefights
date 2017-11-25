def palindromeRearranging(arr):
    return len([i for i in set(arr) if arr.count(i)%2]) < 2


"""
Given a string, find out if its characters can be rearranged to form a
palindrome.

Example

For inputString = "aabb", the output should be
palindromeRearranging(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.
"""
