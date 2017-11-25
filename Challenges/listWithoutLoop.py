"""
You are given n, return an array ans, composed in such way:
ans = [n, n - 5, n - 10, ... , m, m + 5, ... , n - 5, n], where m stands for
the first non-positive integer obtained by subtractions.
Try to solve it without any loop.
"""
def listWithoutLoop(n):
    r = []
    x = n
    while x > 0:
        r.append(x)
        x -= 5
    while x <= n:
        r.append(x)
        x += 5
    return r
