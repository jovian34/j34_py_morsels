from collections.abc import Hashable


def uniques_only(values):
    uniques_hashable = set()
    uniques_unhashable = []
    for value in values:
        if isinstance(value, Hashable):
            if value not in uniques_hashable:
                uniques_hashable.add(value)
                yield value
        else:
            if value not in uniques_unhashable:
                uniques_unhashable.append(value)
                yield value



