from itertools import zip_longest
from random import randbytes


def interleave(first, *args):
    fill_value = randbytes(32)
    zipped = zip_longest(first, *args, fillvalue=fill_value)
    for values in zipped:
        for value in values:
            if value != fill_value:
                yield value






