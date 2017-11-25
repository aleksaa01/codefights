def commonCharacterCount(s1, s2):
    res = 0
    for i in set(s1):
        if i in s2:
            res += min(s1.count(i), s2.count(i))
    return res


"""
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".
"""
