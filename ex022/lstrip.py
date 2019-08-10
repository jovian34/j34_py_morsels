
def lstrip(values, strip):
    stripping = True
    for value in values:
        if value == strip and stripping:
            continue
        yield value
        stripping = False
