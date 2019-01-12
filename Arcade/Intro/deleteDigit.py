def deleteDigit(n):
    n = [i for i in str(n)]
    max_digit = 0

    for i in range(len(n)):
        current_digit = int("".join(n[:i] + n[i + 1:]))
        if current_digit > max_digit:
            max_digit = current_digit

    return max_digit


"""
Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.

Example

    For n = 152, the output should be
    deleteDigit(n) = 52;
    For n = 1001, the output should be
    deleteDigit(n) = 101.

"""