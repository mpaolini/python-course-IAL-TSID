def find_longest_word(words):
    longest_len = 0
    for word in words:
        if len(word) > longest_len:
            longest_len = len(word)
    return longest_len


def filter_long_words(words, length):
    long_words = []
    for word in words:
        if len(word) > length:
            long_words.append(word)
    return long_words

    return [word for word in words
            if len(word) > length]
