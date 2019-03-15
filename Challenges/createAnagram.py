def createAnagram(s, t):
    schars = [0] * 26
    tchars = [0] * 26

    # we can do this because length of s and t are guaranteed to be equal.
    for i, j in zip(s, t):
        schars[ord(i) - 65] += 1
        tchars[ord(j) - 65] += 1

    num = 0
    for i in range(26):
        x = tchars[i]
        y = schars[i]
        if x > y:
            num += x - y

    return num


"""
You are given two strings s and t of the same length, consisting of uppercase English letters. 
Your task is to find the minimum number of "replacement operations" 
needed to get some anagram of the string t from the string s. 
A replacement operation is performed by picking exactly one character from the string s and 
replacing it by some other character.

Example

For s = "AABAA" and t = "BBAAA", the output should be
createAnagram(s, t) = 1;
For s = "OVGHK" and t = "RPGUC", the output should be
createAnagram(s, t) = 4.
"""