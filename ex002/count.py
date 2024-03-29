
def count_words(words):
    word_list = words.split()
    word_list = [word.strip(' ¿!,.?:;').lower() for word in word_list]
    word_dict = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict