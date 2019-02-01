from collections import OrderedDict


def firstNotRepeatingCharacter(s):
    d = OrderedDict()
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 0

    for k, v in d.items():
        if v == 0:
            return k

    return '_'


"""
Given a string s consisting of small English letters, find and return the first instance of a
non-repeating character in it. If there is no such character, return '_'.

Example

For s = "abacabad", the output should be
firstNotRepeatingCharacter(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

For s = "abacabaabacaba", the output should be
firstNotRepeatingCharacter(s) = '_'.

There are no characters in this string that do not repeat.
"""