from math import pi


class Circle:

    def __init__(self, radius=1):
        self._radius = radius

    def __str__(self):
        return f'Circle({self._radius})'

    def __repr__(self):
        return f'Circle({self._radius})'

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        self._radius = value / 2

    @property
    def area(self):
        return self._radius ** 2 * pi

    @area.setter
    def area(self, value):
        raise AttributeError("The area cannot be changed directly")
