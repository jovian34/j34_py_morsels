from itertools import zip_longest
from random import randbytes


def interleave1(first_iter, second_iter):
    first_dict = {}
    second_dict = {}
    for i, first_item in enumerate(first_iter):
        first_dict[i] = first_item
    for i, secondary in enumerate(second_iter):
        second_dict[i] = secondary
    for key, value in first_dict.items():
        yield value
        yield second_dict[key]


def interleave2(first, second):
    first_iter = iter(first)
    second_iter = iter(second)
    try:
        while True:
            yield next(first_iter)
            yield next(second_iter)
    except StopIteration:
        pass


def interleave3(first, *args):
    all_groups = [iter(first)]
    for arg in args:
        all_groups.append(iter(arg))
    try:
        while True:
            for group in all_groups:
                yield next(group)
    except StopIteration:
        pass


def interleave(first, *args):
    fill_value = randbytes(32)
    zipped = zip_longest(first, *args, fillvalue=fill_value)
    for values in zipped:
        for value in values:
            if value != fill_value:
                yield value






