def differentSymbolsNaive(s):
    lets = [0] * 26

    for i in s:
        lets[ord(i) - 97] = 1

    return sum(lets)


"""
Given a string, find the number of different characters in it.

Example

For s = "cabca", the output should be
differentSymbolsNaive(s) = 3.

There are 3 different characters a, b and c.
"""