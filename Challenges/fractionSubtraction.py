def fractionSubtraction(a, b):
    den = a[1] * b[1]
    nom = a[0] * b[1] - b[0] * a[1]

    gcd = math.gcd(den, nom)

    return [nom / gcd, den / gcd]


"""
Implement a function that can subtract two reduced fractions and produce a new one.

Example

For a = [7, 10] and b = [3, 10], the output should be
fractionSubtraction(a, b) = [2, 5].

7/10 - 3/10 = 4/10 = 2/5, so the answer is [2, 5].
"""