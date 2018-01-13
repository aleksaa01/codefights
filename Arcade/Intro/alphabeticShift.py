def alphabeticShift(inputString):
    ans = []
    for i in inputString:
        if ord(i) < 122:
            ans.append(chr(ord(i) + 1))
        else:
            ans.append('a')
    return "".join(ans)


"""
Given a string, replace each its character by the next one in the English
alphabet (z would be replaced by a).

Example

For inputString = "crazy", the output should be
alphabeticShift(inputString) = "dsbaz".
"""
