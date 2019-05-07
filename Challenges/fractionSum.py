def fractionSum(a, b):
    den = a[1] * b[1]
    nom = a[0] * b[1] + b[0] * a[1]

    gcd = math.gcd(den, nom)

    return [nom / gcd, den / gcd]


"""
Implement a function that can sum two reduced fractions and produce a new one.

Example

For a = [3, 5] and b = [7, 5], the output should be
fractionSum(a, b) = [2, 1].

3 / 5 + 7 / 5 = 10 / 5 = 2 / 1, so the answer is [2, 1]
"""