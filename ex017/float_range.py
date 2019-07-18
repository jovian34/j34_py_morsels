def float_range(start, stop='tester', step=1):
    if stop == 'tester':
        start, stop = 0, start
    if step < 0:
        while start > stop:
            yield start
            start = step + start
    else:
        while start < stop:
            yield start
            start += step


if __name__ == "__main__":
    result = float_range(5, 1, -1)
    for value in result:
        print(value)
