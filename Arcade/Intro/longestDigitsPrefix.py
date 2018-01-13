def longestDigitsPrefix(inputString):
    res = []
    for i in inputString:
        if i.isdigit():
            res.append(i)
        else:
            break
    return "".join(res)



"""
Given a string, output its longest prefix which contains only digits.

Example

For inputString="123aa1", the output should be
longestDigitsPrefix(inputString) = "123".
"""
