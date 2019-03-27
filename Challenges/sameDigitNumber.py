def sameDigitNumber(n):
    first_digit = n % 10
    while n > 0:
        if n % 10 != first_digit:
            return False

        n //= 10

    return True


"""
Given an integer, check that all the digits in the number are the same.

Example

For n = 1111, the output should be
sameDigitNumber(n) = true;
For n = 1122, the output should be
sameDigitNumber(n) = false.
"""