
def rec_deep_add(values, total):
    for value in values:
        try:
            total += value
        except TypeError:
            total = rec_deep_add(value, total)
    return total


def deep_add(args, start=0):
    return rec_deep_add(values=args, total=start)


