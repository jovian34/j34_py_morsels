from collections import Counter


def multimax(iter_input, key=None):
    output = []

    if key:
        iterable = [key(item) for item in iter_input]
    else:
        iterable = iter_input

    counts = Counter(iterable)

    try:
        maximum = max(counts)
    except ValueError:
        return output
    multi = counts[maximum]
    for i in range(multi):
        output.append(maximum)

    if key:
        output = [item for item in iter_input if key(item) == maximum]

    return output




