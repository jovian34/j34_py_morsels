def generate_items(sequence):
    compare = ['shajdDhk3hd@Wjdjk3dh#3dkd3^3h5Dj3h5-435jhj43h5k&j3nk*k3edn3ke']
    for item in sequence:
        if item != compare:
            yield item
        compare = item


def compact(items):
    return generate_items(items)