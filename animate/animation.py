from graphics import GraphWin, Rectangle, Point


class Animation:
    def __init__(self, characters, script):
        self.window = GraphWin()
        self.characters = characters
        self.script = script
        self.time = 0

    def advance(self):
        self.script[self.time]()
        self.time += 1

    def show(self):
        for character in self.characters:
            character.draw(self.window)
        self.window.getMouse()
        self.window.close()


def test():
    window = GraphWin()
    r = Rectangle(Point(1, 1), Point(100, 100))
    r.setFill("red")
    r.draw(window)
    window.getMouse()
    window.close()


def test2():
    r = Rectangle(Point(1, 1), Point(100, 100))
    window = GraphWin()
    anim = Animation([r], [None])
    anim.show()


if __name__ == "__main__":
    test2()
