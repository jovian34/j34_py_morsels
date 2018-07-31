

def matrix_from_string(x: str) -> list:
    line_split_str = x.split('\n')

    output_list = []

    for i in range(len(line_split_str)):
        output_list.append([])
        numbers = line_split_str[i].split()
        for number in numbers:
            output_list[i].append(int(number.strip()))

    return output_list
