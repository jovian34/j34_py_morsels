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


if __name__ == "__main__":
    items = uniques_only([2, 4, 2, 2, 34, 45, [11, 22, 33], 22, [11, 22, 33],
                          34, 45, [11, 44, 33], 22, 11])
    for item in items:
        print(item)
