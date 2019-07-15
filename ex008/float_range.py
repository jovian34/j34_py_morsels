def float_range(*args):
    if len(args) == 1:
        current = 0.0
        while current < args[0]:
            yield current
            current += 1.0
    if len(args) == 2:
        current = args[0]
        while current < args[1]:
            yield current
            current += 1.0
    if len(args) == 3:
        current = args[0]
        if args[2] > 0:
            while current < args[1]:
                yield current
                current += args[2]
        else:
            while current > args[1]:
                yield current
                current += args[2]

if __name__ == "__main__":
    result = float_range(12.0, 5.0, -0.5)
    for value in result:
        print(value)
