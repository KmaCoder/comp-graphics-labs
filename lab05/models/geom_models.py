class Point:
    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = float(z)

    def __copy__(self):
        return Point(self.x, self.y, self.z)

    def __add__(self, other: 'Point'):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        return Point(self.x * other, self.y * other, self.z * other)

    def __sub__(self, other: 'Point'):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def swap_xy(self):
        self.x, self.y = self.y, self.x


class Line:
    def __init__(self, start: Point, end: Point, color):
        self.start = start
        self.end = end
        self.color = color


class Circle:
    def __init__(self, center: Point, radius: int, color):
        self.center = center
        self.radius = radius
        self.color = color


class Triangle:
    def __init__(self, p0: Point, p1: Point, p2: Point, color):
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
        self.color = color

    def sort_vertices(self):
        if self.p0.y > self.p1.y:
            self.p0, self.p1 = self.p1, self.p0
        if self.p0.y > self.p2.y:
            self.p0, self.p2 = self.p2, self.p0
        if self.p1.y > self.p2.y:
            self.p1, self.p2 = self.p2, self.p1

    def is_height_zero(self):
        return self.p0.y == self.p1.y and self.p0.y == self.p2.y

    def get_height(self) -> int:
        """
        Vertices must be sorted before calling this function
        :return:
        """
        return int(self.p2.y - self.p0.y)
