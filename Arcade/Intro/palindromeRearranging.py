"""
Given a string, find out if its characters can be rearranged to form a
palindrome.
"""

def palindromeRearranging(arr):
    return len([i for i in set(arr) if arr.count(i)%2]) < 2
