
def interleave(first_iter, second_iter):
    first_dict = {}
    second_dict = {}
    for i, first_item in enumerate(first_iter):
        first_dict[i] = first_item
    for i, second_item in enumerate(second_iter):
        second_dict[i] = second_item
    for key, value in first_dict.items():
        yield value
        yield second_dict[key]


