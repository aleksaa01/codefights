def arrayMode(sequence):
    counts = [0] * 1001
    for i in sequence:
        counts[i] += 1

    max_value = counts[0]
    index = 0
    for c, v in enumerate(counts):
        if v >= max_value:
            max_value = v
            index = c

    return index


"""
Given array of integers, find its mode.

Example

For sequence = [1, 3, 3, 3, 1], the output should be
arrayMode(sequence) = 3;
For sequence = [1, 3, 2, 1], the output should be
arrayMode(sequence) = 1.
"""