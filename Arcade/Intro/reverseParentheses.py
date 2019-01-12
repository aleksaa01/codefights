def reverseInParentheses(inputString):
    cur_sequence = ''
    stack = []
    for i in range(len(inputString)):
        if inputString[i] == '(':
            stack.append(cur_sequence)
            stack.append('(')
            cur_sequence = ''
        elif inputString[i] == ')':
            while True:
                temp = stack.pop()
                if temp == '(':
                    cur_sequence = cur_sequence[::-1]
                    stack.append(cur_sequence)
                    break
                else:
                    cur_sequence = temp + cur_sequence
            cur_sequence = ''
        else:
            cur_sequence += inputString[i]

    if len(cur_sequence) > 0:
        stack.append(cur_sequence)

    return "".join(stack)


"""
Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.
"""
