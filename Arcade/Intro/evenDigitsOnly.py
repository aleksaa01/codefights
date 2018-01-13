def evenDigitsOnly(n):
    while n>0:
        if (n % 10)%2 != 0:
            return False
        n //= 10
    return True


"""
Check if all digits of the given integer are even.

Example

For n = 248622, the output should be
evenDigitsOnly(n) = true;
For n = 642386, the output should be
evenDigitsOnly(n) = false.
"""
