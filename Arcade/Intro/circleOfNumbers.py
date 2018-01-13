def circleOfNumbers(n, firstNumber):
    mid = n // 2
    return mid+firstNumber if firstNumber < mid else abs(mid-firstNumber)


"""
Consider integer numbers from 0 to n - 1 written down along the circle in such
a way that the distance between any two neighbouring numbers is equal
(note that 0 and n - 1 are neighbouring, too).

Given n and firstNumber, find the number which is written in the radially
opposite position to firstNumber.

Example

For n = 10 and firstNumber = 2, the output should be
circleOfNumbers(n, firstNumber) = 7.
"""
