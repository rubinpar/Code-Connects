class TicTacBoard:
    """
        Implements a square tic-tac-toe board of any size
    """
    def __init__(self, board_size=3):
        self.board_size = board_size
        self.board = [[" "] * self.board_size for _ in range(self.board_size)]

    def has_won(self):
        """ Returns true if someone has won """
        for row in self.board:
            if row == ["O"]*self.board_size or row == ["X"]*self.board_size:
                return True

        for column_number in range(self.board_size):
            if column_number == ["O"]*self.board_size or column_number == ["X"]*self.board_size:
                return True

    def random_square(self):
        # picks at a random a square that's empty
        pass

    def __str__(self):
        out = ""
        for i, row in enumerate(self.board):
          out += "|".join(row) + "\n"
          if (i != self.board_size-1):
            out += (2 * self.board_size - 1) * "-" + "\n"
        return out


def play():
    print("Hi! Welcome to tic-tac-toe! Let's play!")
    board_size = int(input("How big would you like the board to be? "))

    # example:
    board = TicTacBoard(board_size)
    print(board)

    # tasks from July 28
    # 1. board print out prettily, dividing lines and formatted like tic tac toe
    # 2. converting from the user coordinate to the 2d list coordinate,
    #       integer division (//) and remainders (%)
    # 3. take user input and update the board
    # 4. figure out when someone has won
    # 5. make the computer play

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
