class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __copy__(self):
        return Point(self.x, self.y)

    def swap_xy(self):
        self.x, self.y = self.y, self.x

    def swap_with_point(self, p: 'Point'):
        self.x, p.x = p.x, self.x
        self.y, p.y = p.y, self.y


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

    def normalize_vertices(self):
        if self.p1.y > self.p1.y:
            self.p0.swap_with_point(self.p1)
        if self.p0.y > self.p2.y:
            self.p0.swap_with_point(self.p2)
        if self.p1.y > self.p2.y:
            self.p1.swap_with_point(self.p2)
