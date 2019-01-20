from collections import deque


def tail(seq, n):
    """Return the last n items of given iterable."""
    if n <= 0:
        return []
    else:
        return list(seq)[-n:]


def tail_deque(iterable, n):
    """Return the last n items of given iterable.
    this is the more efficient solution given
    by the author of the excercise"""
    if n <= 0:
        return []
    return list(deque(iterable, maxlen=n))