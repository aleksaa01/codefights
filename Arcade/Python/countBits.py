"""
Implement a function that, given an integer n, uses a specific method on it
and returns the number of bits in its binary representation.

Note: in this task and most of the following tasks you will be given a code
snippet with some part of it replaced by the ellipsis (...).
Only this part is allowed to be changed.
"""

def countBits(n):
    return n.bit_length()
