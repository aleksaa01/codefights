def powersOfPrime23(p):
    n = 31
    m = 31
    for i in range(30):
        for j in range(30):
            if abs(2 ** i - 3 ** j) == p and i < n:
                n, m = i, j
                return [n, m]

    return []


"""
Given a prime number p, your task is to find powers of 2 and 3 so that |2n - 3m| = p.
Return the exponents as an array of the form [n, m].

If it's not possible to express p in this form, return [].

If there are multiple possible ways to express p in this form, return the one with the
smallest value of n (ie: the one with the lowest power of 2).

Example

    For p = 37 the output should be powersOfPrime23(p) = [6, 3].

    |26 - 33| = |64 - 27| = 37
    So since n = 6 and m = 3, the answer is [6, 3].

    For p = 113 the output should be powersOfPrime23(p) = [].

    It's not possible to express 113 in the form |2n - 3m|.

    For p = 5 the output should be powersOfPrime23(p) = [2, 2].

    There are multiple ways to express 5 as an absolute difference between a power of 2 and a power of 3:
        |22 - 32| = |4 - 9| = |-5| = 5
        |23 - 31| = |8 - 3| = |5| = 5
        |25 - 33| = |32 - 27| = |5| = 5

    Out of all the possible options, the lowest power of 2 is when n = 2 and m = 2, so the answer is [2, 2].

"""