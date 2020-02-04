class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def swap_xy(self):
        self.x, self.y = self.y, self.x

    def swap_with_point(self, p: 'Point'):
        self.x, p.x = p.x, self.x
        self.y, p.y = p.y, self.y
