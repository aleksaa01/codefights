def reduceString(inputString):
    length = len(inputString)
    for i in range(length // 2):
        if inputString[i] != inputString[length - i - 1]:
            return inputString[i:length - i]

    return ""


"""
You are given a string.
Remove its first and last characters until the string is empty or the first and the last characters are not equal.
Output the resulting string.
"""