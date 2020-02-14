from lab06.models.color import Color
from lab06.models.point import Point


class Line:
    def __init__(self, start: Point, end: Point, color: Color):
        self.start = start
        self.end = end
        self.color = color
