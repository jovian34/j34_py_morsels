
def is_anagram(word1: str, word2: str) -> bool:
    letters1 = [letter for letter in word1.lower()]
    letters2 = [letter for letter in word2.lower()]
    letters1.sort()
    letters2.sort()
    if letters1 == letters2:
        return True
    else:
        return False
