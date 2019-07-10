from graphics import GraphWin, Rectangle, Point
import time
from shape import Square


class Animation:
    def __init__(self, characters, script, delay=1, iterations=100):
        self.window = GraphWin()
        self.characters = characters
        self.script = script
        self.time = 0
        self.delay = delay
        self.iterations = iterations

    def advance(self):
        for character in self.characters:
            for task in self.script[self.time][character]:
                task(character)
        self.time += 1

    def show(self):
        for i in range(self.iterations):
            for character in self.characters:
                character.undraw()
                character.draw(self.window)
            self.advance()
            time.sleep(self.delay)
        self.window.getMouse()
        self.window.close()


def test():
    window = GraphWin()
    window.setCoords(0, 0, 10, 10)
    r = Rectangle(Point(1, 1), Point(2, 2))
    r.setFill("red")
    r.draw(window)
    for i in range(10):
        time.sleep(1)
        r.undraw()
        r.move(1, 0)
        r.draw(window)
    window.getMouse()
    window.close()


def test2():
    r = Rectangle(Point(1, 1), Point(100, 100))
    window = GraphWin()
    anim = Animation([r], [None])
    anim.show()


def test3():
    s = Square("red", 1, 1, 3)
    script = [{s: [lambda o: o.move(0.5, 0)]} for _ in range(100)]
    anim = Animation([s], script, delay=0.1)
    anim.window.setCoords(0, 0, 20, 20)
    anim.show()


if __name__ == "__main__":
    test3()
