from collections import Counter


def multimax(iter_input, key=None):
    output = []

    if key:
        iterable = [key(item) for item in iter_input]
    else:
        iterable = iter_input

    counts = Counter(iterable)

    print(f"Inital counts are {counts}")
    try:
        maximum = max(counts)
        print(f"The maximum is {maximum}")
    except ValueError:
        print("This should only happen if empty")
        return output
    multi = counts[maximum]
    print(f"The maximum happens {multi} times.")
    for i in range(multi):
        output.append(maximum)
    print(f"The final output is {output}")

    if key:
        output = [item for item in iter_input if key(item) == maximum]

    return output

if __name__ == "__main__":
    multimax([1, 4, 2, 4, 3])
    multimax([])
    multimax([[0], [1], [], [0, 1], [1]])


