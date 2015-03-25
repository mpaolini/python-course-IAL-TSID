# coding: utf-8

translations = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}

def translate(sentence):
    translated_words = []
    for word in sentence.split():
        if word in translations:
            translated_words.append(translations[word])
        else:
            translated_words.append(word)
    return ' '.join(translated_words)
