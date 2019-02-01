def firstNotRepeatingCharacter(s):
    """New solution uses cache friendly data structure"""

    # even positions = number of characters
    # odd positions = last occurrence of that character
    scounter = [0] * 52

    for i in range(len(s)):
        char_pos = (ord(s[i]) - 97) * 2
        scounter[char_pos] += 1
        scounter[char_pos + 1] = i

    last_occurrence = len(s)
    for i in range(0, 52, 2):
        if scounter[i] == 1 and scounter[i + 1] < last_occurrence:
            last_occurrence = scounter[i + 1]

    if last_occurrence < len(s):
        return s[last_occurrence]

    return '_'



"""
Note: Write a solution that only iterates over the string once and uses O(1) additional memory, 
since this is what you would be asked to do during a real interview.

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