import math

class Vector:
    def __init__(self, x, y=None, z=None):
        if y is None:
            self.x, self.y, self.z = x[0], x[1], x[2]
        else:
            self.x, self.y, self.z = x, y, z
    
    def __repr__(self):
        return f'<{self.x}, {self.y}, {self.z}>'

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def to_tuple(self):
        return (self.x, self.y, self.z)

    def cross(self, other):
        return Vector(self.y * other.z - self.z * other.y, 
                    self.z * other.x - self.x * other.z, 
                    self.x * other.y - self.y * other.x)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    @property
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)


import pytest

@pytest.fixture
def examples():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    return matrix

def test_q(examples):
    # Should correctly display coordinates
    v = Vector(examples[1])
    assert v.x == 4
    assert v.y == 5
    assert v.z == 6
    # Should handle array representation
    assert Vector(examples[2]).to_tuple() == tuple(examples[2])
    # Should handle string representation
    assert str(Vector(examples[1])) == "<4, 5, 6>"
    # Should handle addition
    assert Vector(examples[0]) + Vector(*examples[1]) == Vector(5, 7, 9)
    # Should handle subtraction
    assert Vector(examples[0]) - Vector(*examples[2]) == Vector(-6, -6, -6)
    # Should handle cross product
    assert Vector(examples[0]).cross(Vector(*examples[1])) == Vector(-3, 6, -3)
    # Should handle dot product
    assert Vector(examples[1]).dot(Vector(*examples[2])) == 122
    # Should handle magnitude
    assert Vector(examples[0]).magnitude == pytest.approx(3.741, 0.001)
    # Both initializiations should result in the same vector
    assert Vector(examples[0]) == Vector(*examples[0])
