from itertools import permutations
def stringsRearrangement(inputArray):
    def check(a, b):
        c = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                c += 1
            if c > 1:
                return False
        if c == 0:
            return False
        return True
    for perm in permutations(inputArray):
        found = True
        for j in range(1, len(perm)):
            if not check(perm[j-1], perm[j]):
                found = False
                break
        if found:
            return True
    return False



"""
Given an array of equal-length strings, check if it is possible to rearrange
the strings in such a way that after the rearrangement the strings at
consecutive positions would differ by exactly one character.

Example

For inputArray = ["aba", "bbb", "bab"], the output should be
stringsRearrangement(inputArray) = false;

All rearrangements don't satisfy the description condition.

For inputArray = ["ab", "bb", "aa"], the output should be
stringsRearrangement(inputArray) = true.

Strings can be rearranged in the following way: "aa", "ab", "bb".
Input/Output

"""
