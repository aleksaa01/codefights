def isBeautifulString(inputString):
    letters = [chr(i) for i in range(ord('a'), ord('z')+1)]
    
    gap = False
    previous = 0
    for i in letters:
        x = inputString.count(i)
        if x == 0:
            if not gap:
                gap = True
        elif x != 0:
            if gap:
                return 0
            elif not previous:
                previous = x
            elif x > previous:
                return 0
        previous = x
    return 1



"""
A string is said to be beautiful if b occurs in it no more times than a;
c occurs in it no more times than b; etc.

Given a string, check whether it is beautiful.

Example

For inputString = "bbbaacdafe", the output should be
isBeautifulString(inputString) = true;
For inputString = "aabbb", the output should be
isBeautifulString(inputString) = false;
For inputString = "bbc", the output should be
isBeautifulString(inputString) = false.
"""
