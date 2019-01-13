def multiply_digits(number):
    res = 1
    while number > 0:
        res *= number % 10
        number //= 10
    return res

def digitsProduct(product):
    for i in range(1, 5000):
        multiplied = multiply_digits(i)
        if multiplied == product:
            return i
    return -1


"""
Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is
equal to product. If there is no such integer, return -1 instead.

Example

    For product = 12, the output should be
    digitsProduct(product) = 26;
    For product = 19, the output should be
    digitsProduct(product) = -1.

"""