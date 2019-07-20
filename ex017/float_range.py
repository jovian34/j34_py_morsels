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

