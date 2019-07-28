game = [[0, 0, 0],
        [0, 0, 0],
        [[0, 0, 0],]
for row in game:
    print(row)

class TicTacBoard:
    def __init__(self):
        pass

    def has_won(self):
        """ Returns true if someone has won """
        pass

    def place_o(self, x, y):
        pass

    def place_x(self, x, y):
        pass

    def random_square(self):
        # picks at a random a square that's empty
        pass


def play():
    print("Hi! Welcome to tic-tac-toe! Let's play!")

choose_character = input("Would you like to be X or O? Type X or O. ")

    # example:
    board = TicTacBoard()
    board.place_o(2, 2)
    # contents = [["_", "_", "_"],
    #             ["_", "x", "o"],
    #             ["_", "_", "_"]]
    # contents[1][1] == "x"
    # contents[1][2] == "o"


    # a = [[1, 2, 3], [4, 5, 6]]
    # a[0] == [1, 2, 3]
    # a[1] == [4, 5, 6]
    # a[1][2] == 5
    # https://snakify.org/en/lessons/two_dimensional_lists_arrays/
    # https://www.tutorialspoint.com/python/python_2darray

    # outline:
    # figure out if they wanna be x or o

    # alternate back and forth. You pick a square to place and then
    # the computer uses the random square to fill out with their symbol

    # always check if whoever just went has won

if __name__ == "__main__":
    play()
