import unicodedata
import string


def is_anagram(word1: str, word2: str) -> bool:
    first_word = word1.lower().replace(' ', '')
    second_word = word2.lower().replace(' ', '')

    translator = str.maketrans('', '', string.punctuation)
    first_word_no_punc = first_word.translate(translator)
    second_word_no_punc = second_word.translate(translator)

    if len(first_word_no_punc) != len(second_word_no_punc):
        False

    letters1 = [
        c for c in unicodedata.normalize('NFD', first_word_no_punc)
        if unicodedata.category(c) != 'Mn'
    ]

    letters2 = [
        c for c in unicodedata.normalize('NFD', second_word_no_punc)
        if unicodedata.category(c) != 'Mn'
    ]

    letters1.sort()
    letters2.sort()

    if letters1 == letters2:
        return True
    else:
        return False
