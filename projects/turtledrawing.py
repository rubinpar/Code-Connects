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
    pencolor(color)

    # calculate sides
    a, b  = base, height
    c = math.sqrt(base**2 + height**2)

    # draw the bottom part
    forward(a)
    angle = 180 - math.degrees(math.asin(b/c))
    left(angle)

    # draw the hypotenuse
    forward(c)
    angle = 180 - math.degrees(math.asin(a/c))
    left(angle)

    # draw the left side
    forward(b)
    left(90)

def draw_roof(base, height, color="black"):
    """
    draws the roof assuming the turtle is in the middle of the top of the house
    """
    #draw the right side
    a, b = base/2, height
    c = math.sqrt(base**2 + height**2)

    # draw the bottom part
    forward(a)
    angle = 180 - math.degrees(math.asin(b/c))
    left(angle)

    # draw the hypotenuse
    forward(c)
    angle = 180 - math.degrees(math.asin(a/c))
    left(angle)

    # don't draw the left side
    penup()
    forward(b)
    left(90)
    pendown()

def draw_house(width, height, roof_base, roof_height):
    # base of the house
    draw_rectangle(width, height, color="#28710D")

    # get to the roof spot
    penup()
    left(90)
    forward(height)
    right(90)
    forward(width/2)
    pendown()

    # draw the roof
    draw_roof(roof_base, roof_height)

#def draw_circle(radius):

shape("turtle")
draw_house(200, 100, 200, 50)
done()
