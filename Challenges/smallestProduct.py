def smallestProduct(a):
    a.sort()
    b = a[0] * a[1] * a[2]
    c = a[0] * a[-1] * a[-2]
    return b if b < c else c


"""
Hi all, I have a tiny challenge for all of you today. I was given some arrays of integers and my mission is to
find the smallest product of 3 elements in an array. I will need your help on this problem.

Please note that our integers can be negative and positive.

Examples

For arr = [1, 2, 3], the output should be smallestProduct(arr) = 6

The only option is 1 * 2 * 3 = 6.

For arr = [-1, 0, -2, 3], the output should be smallestProduct(arr) = 0

There are four possible products, and the smallest one is 0:

-1 * 0 * -2 = 0
-1 * 0 * 3 = 0
-1 * -2 * 3 = 6
0 * -2 * 3 = 0
"""