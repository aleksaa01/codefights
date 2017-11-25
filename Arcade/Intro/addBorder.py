"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.
"""

def addBorder(picture):
    res = picture.copy()
    chars = len(max(picture, key=len)) + 2
    for c,i in enumerate(picture):
        res[c] = '*'*((chars-len(i))//2) + i + '*'*((chars-len(i))//2)
    res.append('*' * chars)
    res.insert(0, '*' * chars)
    return res
