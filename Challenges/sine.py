import math


def sine(theta):
    return math.sin(math.radians(theta))


"""
The sine ratio is a useful math tool, commonly used for finding the vertical component of an angled vector.
It's defined as the ratio between the opposite side and hypotenuse of a right angle triangle.

Given an angle theta in degrees, your task is to return sin(theta).

Example

For theta = 30, the output should be sine(theta) = 0.5.

example 1

In a right triangle with an angle of 30°, there's a 1 : 2 ratio between the opposite side and the hypotenuse,
so the answer is 1 / 2 = 0.5.
"""