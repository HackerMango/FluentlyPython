import math


class Vector:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        return f'Vector({self._x!s}, {self._y!s})'

    def __add__(self, other):
        x = self._x + other._x
        y = self._y + other._y
        return Vector(x, y)

    def __abs__(self):
        return math.sqrt(math.pow(self._x, 2) + math.pow(self._y, 2))

    def __mul__(self, other):
        return Vector(self._x * other, self._y * other)

    def __rmul__(self, other):
        return Vector(self._x * other, self._y * other)


v1 = Vector(3, 4)
v2 = Vector(2, 1)
print(2 * v1)
print(v1 + v2)
print(abs(v1))
