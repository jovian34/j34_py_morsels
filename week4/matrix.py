
def matrix_from_string(x: str) -> list:
    line_split_str = x.split('\n')

    output_list = []

    for i in range(len(line_split_str)):
        output_list.append([])
        numbers = line_split_str[i].split()
        for number in numbers:
            try:  # use integer if possible
                output_list[i].append(int(number.strip()))
            except ValueError:  # otherwise use float if necessary
                output_list[i].append(float(number.strip()))

    while [] in output_list:
        output_list.remove([])

    return output_list
