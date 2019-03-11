def isoscelesTriangle(sides):
    return sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]



"""
Given length of a triangle sides, check if it is isosceles.

Example

For sides = [4, 3, 2], the output should be
isoscelesTriangle(sides) = false;
For sides = [5, 3, 5], the output should be
isoscelesTriangle(sides) = true.
"""