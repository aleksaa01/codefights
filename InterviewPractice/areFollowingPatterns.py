def areFollowingPatterns(strings, patterns):
    pattern_map = dict()  # pattern: string
    string_map = dict()  # string: pattern
    for pattern, string in zip(patterns, strings):
        if pattern in pattern_map:
            if string != pattern_map[pattern]:
                return False
        elif string in string_map:
            if pattern != string_map[string]:
                return False
        pattern_map[pattern] = string
        string_map[string] = pattern

    return True


"""
Given an array strings, determine whether it follows the sequence given in the patterns array.
In other words, there should be no i and j for which strings[i] = strings[j] and patterns[i] ≠ patterns[j]
or for which strings[i] ≠ strings[j] and patterns[i] = patterns[j].

Example

For strings = ["cat", "dog", "dog"] and patterns = ["a", "b", "b"], the output should be
areFollowingPatterns(strings, patterns) = true;
For strings = ["cat", "dog", "doggy"] and patterns = ["a", "b", "b"], the output should be
areFollowingPatterns(strings, patterns) = false.
"""