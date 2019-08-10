from math import sqrt
from cmath import sqrt as csqrt


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


def is_perfect_square(number, *, complex=False) -> bool:
    if not complex:
        try:
            number = float(number)
        except ValueError:
            raise TypeError
        return simple_perfect_square(number)
    else:
        root = csqrt(number)
        if root.imag == 0:
            return root.real.is_integer()
        elif root.real == 0:
            return root.imag.is_integer()
        else:
            if root.real.is_integer():
                if root.imag.is_integer():
                    return True
    return False
