from math import sqrt


def simple_perfect_square(number) -> bool:
    if number < 0:
        return False
    counter = int(sqrt(number) - 2)
    square = 0
    while number > square:
        square = counter ** 2
        if square == number:
            return True
        counter += 1
    return False


def is_perfect_square(number, complex=False) -> bool:
    if not complex:
        if type(number) != int or type(number) != float:
            raise TypeError
        return simple_perfect_square(number)
    else:
        if type(number) == complex:
            return simple_perfect_square(number.real)
        else:
            return simple_perfect_square(number * -1)
    return False
