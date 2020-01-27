from lab02.drawer_bresenham import DrawerBresenham
from lab02.point import Point

drawer = DrawerBresenham(500, 500)
drawer.draw_line(Point(50, 10), Point(250, 100), (200, 100, 100))
drawer.draw_line(Point(150, 10), Point(350, 100), (100, 200, 100))
drawer.draw_line(Point(250, 10), Point(450, 100), (100, 100, 200))
drawer.show_img()
