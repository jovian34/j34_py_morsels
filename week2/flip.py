
def flip_dict_of_lists(d, dict_type=None, key_func=None):
    result = {}

    if type(d) != dict:
        d = dict(d)

    for key, value_list in d.items():
        for value in value_list:
            if key_func:
                value = key_func(value)
            try:
                result[value]
            except KeyError:
                result[value] = []
            result[value].append(key)

    if dict_type:
        result = dict_type(result)

    return result