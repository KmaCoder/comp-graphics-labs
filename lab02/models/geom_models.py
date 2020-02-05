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
