
def with_previous(x, *, fillvalue=None):
    previous = fillvalue
    for i in x:
        yield (i, previous)
        previous = i