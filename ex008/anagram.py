import unicodedata
import string


def is_anagram(word1: str, word2: str) -> bool:
    print(f"Function params are '{word1}' and '{word2}'")

    first_word = word1.lower().replace(' ', '')
    second_word = word2.lower().replace(' ', '')
    print(f"Words that are lower case with no spaces "
          f"are '{first_word}' and '{second_word}'")

    print(string.punctuation)
    translator = str.maketrans('', '', string.punctuation)
    first_word_no_punc = first_word.translate(translator)
    second_word_no_punc = second_word.translate(translator)
    print(f"Words that no punctuation "
          f"are '{first_word_no_punc}' and '{second_word_no_punc}'")

    if len(first_word_no_punc) != len(second_word_no_punc):
        print(f'Lengths are not equal: {len(first_word_no_punc)}'
              f' and {len(second_word_no_punc)}')
        return False

    letters1 = [
        c for c in unicodedata.normalize('NFD', first_word_no_punc)
        if unicodedata.category(c) != 'Mn'
    ]

    letters2 = [
        c for c in unicodedata.normalize('NFD', second_word_no_punc)
        if unicodedata.category(c) != 'Mn'
    ]

    print(f"After removing accents: '{letters1}' and '{letters2}'")

    letters1.sort()
    letters2.sort()
    print(f"After sorting: '{letters1}' and '{letters2}'")

    if letters1 == letters2:
        return True
    else:
        return False


def is_anagram_new(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False

    letters1 = [letter for letter in word1.lower()]
    letters2 = [letter for letter in word2.lower()]

    for letter in letters1:
        if letter in letters2:
            letters2.remove(letter)
            letters1.remove(letter)
        else:
            return False

    return True
