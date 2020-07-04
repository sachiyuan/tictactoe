import numpy
# X = 1, O = 2


class Board:
    def __init__(self):
        self.layout = numpy.zeros((3, 3))

    def insert(self, place, sym):
        symtoval = {'X': 1, 'O': 2}
        if self.layout[place[0], place[1]] == 0:
            self.layout[place[0], place[1]] = symtoval[sym]
            return True
        else:
            print("That space is already taken.")
            return False

    def check_end(self, last_move):
        """
        Check if the game is finished
        :param last_move: Coordinates of the last move (x,y)
        :return result:  True if the game is not over, False if it is
        """
        x = last_move[1]
        y = last_move[0]
        col_result = self.check_column(x)
        row_result = self.check_row(y)
        diag_result = self.check_diagonal((y,x))
        if col_result + row_result + diag_result != 0:
            if col_result == 1 or row_result == 1 or diag_result == 1:
                print("X wins!")
            elif col_result == 2 or row_result == 2 or diag_result ==2:
                print("O wins!")
            else:
                print("Tie!!")
            return True
        else:
            return False
#TODO: Make it so it doesn't end game when column is full if board is not full
    def check_column(self, x):
        """
        Check if column is full and if there is a victor
        :param x: Which column
        :return: return 0 if not full, 1 if X is victor, 2 if O is victor, and 3 if tied
        """
        same = numpy.all(self.layout == self.layout[0, :], axis=0)[x]  # returns whether all values in column x are same
        if same:
            return self.layout[0][x]  # if filled with 0, returns 0, likewise returns corresponding val for X and O
        else:
            for row in self.layout:
                if row[x] == 0:
                    return 0  # if there are any blank spaces, returns 0
            return 3  # if there were no blank spaces, returns 3

    def check_row(self, y):
        """
        Check if row is full and if there is victor
        :param y: Which row
        :return: return 0 if not full, 1 if X is victor, 2 if O is victor, and 3 if tied
        """
        row = self.layout[y]
        if 0 not in row:
            if numpy.all(row == row[0]):  # tests if all the values in a row are the same
                return row[0]  # if filled with X, returns 1 and if filled with O returns 2
            else:
                return 3
        else:
            return 0

    def check_diagonal(self, place):
        """
        Check if the diagonal is full and if there is a victor
        :param place: coordinates of space
        :return: 0 if not full, 1 if X is victor, 2 if 0 is victor, and 3 if tied
        """
        if place[0] == place[1]: #aka if place in {(0,0), (1,1), (2,2)}
            #testing the top left to bottom right diagonal
            diagonal = self.layout.diagonal()
            if 0 not in diagonal:
                if numpy.all(diagonal == diagonal[0]):
                    return diagonal[0]
                else:
                    return 3
            else:
                return 0
        if place in {(0, 2), (1,1), (2,0)}:
            first = self.layout[0,2]
            second = self.layout[1,1]
            third = self.layout[2,0]
            if first == second == third:
                return first
            else:
                if 0 in {first, second, third}:
                    return 0
                else:
                    return 3

    def print_board(self):
        valtosym = {0: ' ', 1: 'X', 2: 'O'}
        board = "\n  {}  |  {}  |  {}   \n".format(valtosym[self.layout[0, 0]], valtosym[self.layout[0, 1]],
                                               valtosym[self.layout[0, 2]]) +\
                    "_____|_____|_____\n"+ \
                    "  {}  |  {}  |  {}  \n".format(valtosym[self.layout[1, 0]],
                                               valtosym[self.layout[1, 1]], valtosym[self.layout[1, 2]]) + \
                    "_____|_____|_____\n" + \
                    "  {}  |  {}  |  {}  \n".format( valtosym[self.layout[2, 0]], valtosym[self.layout[2, 1]],
                                               valtosym[self.layout[2, 2]]) + \
                    "     |     |      "
        print(board)

