def allLongestStrings(inputArray):
    longest = len(max(inputArray, key=len))
    return [i for i in inputArray if len(i)==longest]


"""
Given an array of strings, return another array containing all of its
longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].
"""
