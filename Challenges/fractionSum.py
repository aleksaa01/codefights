def fractionSum(a, b):
    den = a[1] * b[1]
    nom = a[0] * b[1] + b[0] * a[1]

    gcd = math.gcd(den, nom)

    return [nom / gcd, den / gcd]
