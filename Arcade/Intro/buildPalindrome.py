from collections import deque
def buildPalindrome(st):
    ext = deque()
    for i in range(len(st)):
        check = st + "".join(ext)
        if check == check[::-1]:
            return check
        ext.appendleft(st[i])


"""
Given a string, find the shortest possible string which can be achieved by
adding characters to the end of initial string to make it a palindrome.

Example

For st = "abcdc", the output should be
buildPalindrome(st) = "abcdcba".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string st

A string consisting of lowercase latin letters.

Guaranteed constraints:
3 ≤ st.length ≤ 10.
"""
