
def lstrip_func(values, strip):
    stripping = True
    for value in values:
        if strip(value) and stripping:
            continue
        yield value
        stripping = False


def lstrip_not_func(values, strip):
    stripping = True
    for value in values:
        if value == strip and stripping:
            continue
        yield value
        stripping = False


def lstrip(values, strip):
    if callable(strip):
        return lstrip_func(values, strip)
    else:
        return lstrip_not_func(values, strip)

