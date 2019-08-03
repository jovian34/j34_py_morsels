def default(x):
    return x


def group_by(values, key_func=default):
    output = {}
    for value in values:
        try:
            output[key_func(value)].append(value)
        except KeyError:
            output[key_func(value)] = [value]
    return output
