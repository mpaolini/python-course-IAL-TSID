''' Exercise 1.

see here https://trello.com/c/AmzD7uRa
'''

def longest_word(*words):
    '''Find longest word.

    Args:
       *words a variable numer of strings

    Returns:
       a single string (the longest one!)
    '''
    parola = None
    for word in words:
        if (parola is None or
                len(word) >= len(parola)):
            parola = word
    return parola


def longest_word_2(*words):
    parola = words[0] if words else None
    for word in words:
        if len(word) >= len(parola):
            parola = word
    return parola


def longest_word_3(*words):
    words = sorted(words, key=len, reverse=True)
    return words[0] if words else None
