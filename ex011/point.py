

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
