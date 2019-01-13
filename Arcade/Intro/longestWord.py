def longestWord(text):
    longest_word = []
    current_word = []
    for i in text:
        if i.isalpha():
            current_word.append(i)
        else:
            if len(current_word) > len(longest_word):
                longest_word = current_word.copy()
            current_word = []

    if len(current_word) > len(longest_word):
        longest_word = current_word.copy()

    return ''.join(longest_word)


"""
Define a word as a sequence of consecutive English letters. Find the longest word from the given string.

Example

For text = "Ready, steady, go!", the output should be
longestWord(text) = "steady".
"""