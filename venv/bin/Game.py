from Board import Board
import math


def game():
    single_player = False
    players = input("Please input 1 or 2 players.\n")
    if players == "1":
        print("You have selected single-player mode.")
        single_player = True
    elif players != "2":
        print("That was not one of the options. You have been defaulted to 2 player mode.")
    else:
        print("You have selected 2 player mode.")
    playing = True
    board = Board()

    example_board = "\n  {}  |  {}  |  {}   \n".format('1', '2', '3') +\
                    "_____|_____|_____\n"+ \
                    "  {}  |  {}  |  {}  \n".format('4', '5', '6', ) + \
                    "_____|_____|_____\n" + \
                    "  {}  |  {}  |  {}  \n".format('7', '8', '9') + \
                    "     |     |      "
    print("When it is your turn, indicate which space you would like to use by inputting the number of that space")
    print(example_board)
    print("You may not use a space which has already been filled")
    print("The game will end when one player has filled a row or column with their symbol, or when the board is filled")
    x_turn = True
    playing = True
    if not single_player:
        print("X goes first")

        while playing:
            board.print_board()
            symbol = "O"
            success = False
            x, y = 0, 0

            if x_turn:
                symbol = "X"
            place = input("Where would you like to go?\n")
            try:
                place = int(place)
                if 0 < place < 10:
                    place -= 1
                    y = place // 3
                    x = place % 3
                    success = board.insert((y, x), symbol)
                else:
                    print("Please input a number on the board")
                if not success:
                    print("Please input a space that has not been taken.")
                else:
                    x_turn = not x_turn
                    if board.check_end((y, x)):
                        board.print_board()
                        playing = False
            except ValueError:
                print("Not a valid input. Please try again.")

    else:
        print("You go first.")
        board.print_board()
        symbol = "O"
        success = False
        if x_turn:
            symbol = "X"
            place = input("Where would you like to go?\n")
            try:
                place = int(place)
                if 0 < place < 10:
                    place -= 1
                    y = place // 3
                    x = place % 3
                    success = board.insert((y, x), symbol)
                else:
                    print("Please input a number on the board")
                if not success:
                    print("Please input a space that has not been taken.")
                else:
                    x_turn = not x_turn
                    if board.check_end((y, x)):
                        board.print_board()
                        playing = False
            except ValueError:
                print("Not a valid input. Please try again.")
        else:
            action = AlphaBetaSearch(board)
            success = board.insert(action, symbol)
            if not success:
                print("Whelp, something went wrong")
            else:
                x_turn = not x_turn
                if board.check_end((y, x)):
                    board.print_board()
                    playing = False


def AlphaBetaSearch(state): # return action as tuple coordinates
    v = MAXVAL(state, -math.inf, math.inf)
    actions = Actions(state)  # dictionary
    return actions[v]

def Actions(state):
    #return a dictionary with actions with corresponding evaluations
    actions = {}
    return actions

def MAXVAL(state, alpha, beta):
    if CUTOFF(state, depth):
        return EVAL(state)
    v = -math.inf
    for a in Actions(state):  #figure out if iterating through keys or values
        v = max(v, MINVAL(RESULT(state, a), alpha, beta))
        if v >= beta:
            return v
        a = max(alpha, v)
    return v

def MINVAL(state, alpha, beta):
    if CUTOFF(state, depth):
        return EVAL(state)
    v = math.inf
    for a in Actions(state):
        v = min(v, MAXVAL(RESULT(state, a), alpha, beta))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v


def EVAL(state):
    # evaluate state either victory or not if terminal or heuristic if not
    return 0


def RESULT(state, action):
    # show the result of the action on the state)
    newstate = 0 #copy of state and then perform action but don't copy reference
    return newstate



game()