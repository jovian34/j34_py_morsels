
def minmax(list_of_values):
    first_item = True
    min_val = None
    for value in list_of_values:
        if first_item:
            min_val = value
            max_val = value
            first_item = False
            continue
        elif value > max_val:
            max_val = value
        elif value < min_val:
            min_val = value
    if min_val is None:
        raise ValueError
    else:
        return min_val, max_val

