def isPower(n):
    for i in range(1, 21):
        for j in range(2, 21):
            x = i ** j
            if x > 400:
                break
            elif x == n:
                return True
    return False



"""
Determine if the given number is a power of some non-negative integer.

Example

For n = 125, the output should be
isPower(n) = true;
For n = 72, the output should be
isPower(n) = false.
"""