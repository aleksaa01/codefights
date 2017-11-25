def reverseParentheses(s):
    if '(' not in s:
        return s
    else:
        i_l = s.rfind('(')
        tmp_s = s[i_l:]
        i_r = tmp_s.find(')')
        new_s = tmp_s[:i_r+1]
        new_s = new_s[1:]
        new_s = new_s[:-1]
        new_s = new_s[::-1]
        new_change_string = s[:i_l] + new_s + s[i_l+i_r+1:]
        return reverseParentheses(new_change_string)


"""
You have a string s that consists of English letters, punctuation marks,
whitespace characters, and brackets. It is guaranteed that the parentheses in
s form a regular bracket sequence.

Your task is to reverse the strings contained in each pair of matching
parentheses, starting from the innermost pair. The results string should not
contain any parentheses.

Example

For string s = "a(bc)de", the output should be
reverseParentheses(s) = "acbde".
"""
