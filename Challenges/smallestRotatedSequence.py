def smallestRotatedSequence(seq):
    # Booth's algorithm.
    seq += seq
    slen = len(seq)
    prefix = [-1] * slen
    index = 0
    for i in range(1, slen):
        j = seq[i]
        cur = prefix[i - index - 1]

        while cur != -1 and j != seq[index + cur + 1]:
            if j < seq[index + cur + 1]:
                index = i - cur - 1
            cur = prefix[cur]

        if j != seq[index + cur + 1]:
            if j < seq[index]:
                index = i
            prefix[i - index] = -1
            continue

        prefix[i - index] = cur + 1

    return index


"""
A sequence, e.g. ABCD, can be rotated to make another sequence, e.g. BCDA.
Find the starting index of the lexicographically smallest rotated sequence. (If there are ties, use the smallest index)

Example

smallestRotatedSequence("DBAC") = 2
There are four different rotated sequences: DBAC, BACD, ACDB, CDBA. But ACDB is the smallest. The starting index is 2.
"""