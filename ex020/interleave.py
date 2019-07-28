from collections.abc import Iterator


def interleave(alpha, bravo):
    if not isinstance(alpha, Iterator):
        alpha = iter(alpha)
    if not isinstance(bravo, Iterator):
        bravo = iter(bravo)
    for item in alpha:
        yield item
        yield next(bravo)
