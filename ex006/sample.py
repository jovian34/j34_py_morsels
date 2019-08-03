from string import punctuation
from collections import Counter

with open('cars-original.csv', 'r') as fd:
    print(f"in fd statement")
    delim_lines = []
    for line in fd.readlines():
        for character in line:
            print(f'{character}')
            if character in punctuation:
                print(f"\nPunctuation Found: {character}")
                delim_lines.append(character)
    ct = Counter(delim_lines)
    max_value = max(ct.values())
    for key, value in ct.items():
        if value == max_value:
            new_delimiter = key
    print(f'the new delimiter is: {new_delimiter}')