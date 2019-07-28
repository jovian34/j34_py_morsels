from collections import Counter


def multimax_old(iter_input, key=None):
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

def multimax(iter_input, key=None):
    working_list = [item for item in iter_input]
    try:
        maximum = max(working_list)
    except ValueError:
        working_list = []

    if key:
        working_list = [key(item) for item in iter_input]
        maximum = max(working_list)
        return [
            item
            for item in iter_input
            if key(item) == maximum
        ]

    return [
        item
        for item in working_list
        if item == maximum
    ]


