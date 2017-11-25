"""
Given positive integer numbers a, b and n return the maximum number that can
be obtained by lengthening number a repeatedly no more than n times.

Lengthening number a means appending exactly one digit (in the decimal notation)
to the right hand side of a such that the resulting number is divisible by
number b. If it is impossible to obtain a number that is divisible by b, then
the lengthening operation cannot be performed.
"""
def addDigits(a, b, n):
    for _ in range(n):
        tmp = a
        for i in range(10):
            # print(str(a)+str(i))
            x = int(str(a)+str(i))
            if x % b == 0:
                tmp = x
        a = tmp
    return str(a)
