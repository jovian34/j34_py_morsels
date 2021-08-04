
def all_same(items):
    first_item = True
    check_value = None
    result = True
    for item in items:
        if first_item:
            check_value = item
            first_item = False
        else:
            if item == check_value:
                continue
            else:
                result = False
                break
    return result
