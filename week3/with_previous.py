
def with_previous(x, *, fillvalue=None):

    first = True

    for i in x:
        if first:
            yield (i, fillvalue)
            previous = i
            first = False
        else:
            yield (i, previous)
            previous = i