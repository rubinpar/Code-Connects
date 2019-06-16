# turtle drawing project
from turtle import *
import math

def draw_rectangle(length, width, color="blue"):
    """
    Draw a rectangle from the bottom left corner,
        heading in the turtle direction
    Parameters:
        length: the size of rectangle in x coordinates
        width:  the size of rectangle in y coordinates
    Note: turtle ends by facing the direction he started
    """
    # set the color of the rectangle
    pencolor(color)

    # draws the bottom of rectangle
    forward(length)
    left(90)

    # draw the right side of the rectangle
    forward(width)
    left(90)

    # draw the top side of the rectangle
    forward(length)
    left(90)

    # draw the left side of the rectangle
    forward(width)
    left(90)

def draw_right_triangle(base, height, color="blue"):
    """
    Drawing a right triangle with the right angle where the turtle starts
    Parameters:
        base: x dimension of the right triangle, the bottom part
        height: y dimension of the right triangle, the left vertical part
    """
    # a^2 + b^2 = c^2
    # c = sqrt(a^2 + b^2)
    a, b  = base, height
    c = math.sqrt(a**2 + b**2)
    pencolor(color)

    # draw the bottom part

    # draw the hypotenuse

    # draw the left side

def draw_circle(radius):
    pass

draw_rectangle(100, 50, color="#28710D")
done()
