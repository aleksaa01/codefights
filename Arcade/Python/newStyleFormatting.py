def newStyleFormatting(s):
    res = []
    jump = False
    for c,i in enumerate(s):
        if i == '%' and not jump:
            if s[c+1] in "bcdeEfFgGnosxX":
                res.append('{}')
                jump = True
            elif s[c+1] == '%':
                res.append('%')
                jump = True
        else:
            if jump:
                jump = False
            else:
                res.append(i)
    return "".join(res)


"""
You came to work in a big company as a Senior Python Developer. Unfortunately your team members seem to be quite
old-school: you can see old-style string formatting everywhere in the code, which is not too cool.
You tried to force the team members to start using the new style formatting, but it looks like it will take
some time to persuade them: old habits die hard, especially in old-school programmers.

To show your colleagues that the new style formatting is not that different from the old style, you
decided to implement a function that will turn the old-style syntax into a new one.
Implement a function that will turn the old-style string formating s into a new one so that the following
two strings have the same meaning:

    s % (*args)
    s.format(*args)

Example

For s = "We expect the %f%% growth this week", the output should be
newStyleFormatting(s) = "We expect the {}% growth this week".
"""