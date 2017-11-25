"""
Professor Dillon has another problem for Aalekh today.
He has given him three positive integers a, n and p and wants him to calculate
the remainder when a ^ n! is divided by p. As usual, n! denotes the product of
the first n positive integers.
"""

import math
solveaSmall=lambda a,n,p: pow(a,math.factorial(n),p)
