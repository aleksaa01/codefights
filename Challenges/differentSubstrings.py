def differentSubstrings(inputString):
    substrings = set()
    for i in range(0, len(inputString)):
        for j in range(i, len(inputString)):
            substrings.add(inputString[i:j + 1])

    return len(substrings)


"""
Given a string, find the number of different non-empty substrings in it.

Example

For inputString = "abac", the output should be
differentSubstrings(inputString) = 9.
They are:

"a", "b", "c",
"ab", "ac", "ba",
"aba", "bac",
"abac"
"""