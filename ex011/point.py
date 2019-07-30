

class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return (
            f"Point(x={self.x}, "
            f"y={self.y}, "
            f"z={self.z})"
        )

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        if self.x != other.x:
            return False
        if self.y != other.y:
            return False

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        if self.x != other.x:
            return False
        if self.y != other.y:
            return False
        if self.z != other.z:
            return False
        return True

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Point(x, y, z)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Point(x, y, z)

    def __mul__(self, other):
        x = self.x * other
        y = self.y * other
        z = self.z * other
        return Point(x, y, z)

    def __rmul__(self, other):
        return self.__mul__(other)
