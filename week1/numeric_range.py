
def numeric_range(numbers):
    start = True
    largest = None
    smallest = None

    for number in numbers:
        if start:
            largest = number
            smallest = number
            start = False
        else:
            if number > largest:
                largest = number
            if number < smallest:
                smallest = number

    if start:
        return 0
    else:
        return largest - smallest