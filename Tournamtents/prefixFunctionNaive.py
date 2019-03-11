def prefixFunctionNaive(s):
    slen = len(s)
    lsp = [0] * slen

    i = 1
    prev_lsp_len = 0
    while i < slen:
        if s[i] == s[prev_lsp_len]:
            prev_lsp_len += 1
            lsp[i] = prev_lsp_len
        elif prev_lsp_len != 0:
            prev_lsp_len = lsp[prev_lsp_len - 1]
            continue
        else:
            lsp[i] = 0
        i += 1

    return lsp


"""
Return the value of prefix function for a given string.

Example

For s = "acacbab", the output should be
prefixFunctionNaive(s) = [0, 0, 1, 2, 0, 1, 0].
"""