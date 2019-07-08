class Shape:
    def __init__(self, color):
        self.color = color

class Triangle(Shape):
    def __init__(self, color, point1, point2, point3):
        """
        Creates a Triangle.

        example:
        point1 = (1, 1)
        point2 = (2, 2)
        point3 = (2, 1)
        triangle = Triangle("black", point1, point2, point3)
        """
        Shape.__init__(self, color)
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    def move(self, dx, dy):
        """
        Move the triangle to the right dx (or to left if negative) and
        move it up dy amount (or down if negative)
        """
        self.point1 = (self.point1[0]+dx, self.point1[1]+dy)
        self.point2 = (self.point2[0]+dx, self.point2[1]+dy)
        self.point3 = (self.point3[0]+dx, self.point3[1]+dy)

    def rotate(self, point, amount):
        pass

    def recolor(self, new_color):
        pass

    def scale(self, amount):
        pass
