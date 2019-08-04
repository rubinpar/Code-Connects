from graphics import Rectangle, Point, Polygon
from abc import abstractmethod


class Character:
    def __init__(self):
        pass

    @abstractmethod
    def move(self, dx, dy):
        pass

    @abstractmethod
    def rotate(self, angle, x=0, y=0):
        pass

    @abstractmethod
    def recolor(self, color):
        pass

    @abstractmethod
    def scale(self, amount):
        pass

    @abstractmethod
    def draw(self, window):
        pass

    @abstractmethod
    def undraw(self):
        pass


class Square(Character):
    def __init__(self, color, lower_x, lower_y, size):
        Character.__init__(self)
        self.rect = Rectangle(Point(lower_x, lower_y),
                              Point(lower_x + size, lower_y + size))

    def move(self, dx, dy):
        self.rect.move(dx, dy)

    def rotate(self, angle, x=0, y=0):
        pass

    def recolor(self, color):
        pass

    def scale(self, amount):
        pass

    def draw(self, window):
        self.rect.draw(window)

    def undraw(self):
        self.rect.undraw()


class Triangle(Character):
    def __init__(self, color, point1, point2, point3):
        """
        Creates a Triangle.

        example:
        point1 = (1, 1)
        point2 = (2, 2)
        point3 = (2, 1)
        triangle = Triangle("black", point1, point2, point3)
        """
        Character.__init__(self)
        self.color = color
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.triangle = Polygon(self.point1, self.point2, self.point3)
        self.triangle.setFill(color)

    def move(self, dx, dy):
        """
        Move the triangle to the right dx (or to left if negative) and
        move it up dy amount (or down if negative)
        """
        self.point1 = (self.point1[0]+dx, self.point1[1]+dy)
        self.point2 = (self.point2[0]+dx, self.point2[1]+dy)
        self.point3 = (self.point3[0]+dx, self.point3[1]+dy)
        self.trianglem.move(dx, dy)

    def rotate(self, angle, x=0, y=0):
        pass

    def recolor(self, new_color):
        self.triangle.recolor(new_color)

    def scale(self, amount):
        pass

    def draw(self, window):
        self.triangle.draw(window)

    def undraw(self):
        self.triangle.undraw()
