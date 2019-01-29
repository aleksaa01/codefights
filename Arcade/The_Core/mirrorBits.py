def mirrorBits(a):
    # [:1:-1](go from last to second) is same as
    # [2:][::-1](cut out first two and then reverse)
    return int(bin(a)[:1:-1], 2)


"""
Reverse the order of the bits in a given integer.

Example

For a = 97, the output should be
mirrorBits(a) = 67.

97 equals to 1100001 in binary, which is 1000011 after mirroring, and that is 67 in base 10.

For a = 8, the output should be
mirrorBits(a) = 1.
"""