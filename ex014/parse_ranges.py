
def parse_ranges(range_string: str):
    ranges = range_string.split(',')
    for a_range in ranges:
        start, finish = a_range.split('-')
        start = int(start)
        finish = int(finish)
        output_range = range(start, finish + 1)
        for value in output_range:
            yield value
