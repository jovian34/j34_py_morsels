
def all_same(items):
    first_item = True
    for item in items:
        if first_item:
            check_value = item
            first_item = False
        else:
            if item == check_value:
                continue
            else:
                return False
    return True
