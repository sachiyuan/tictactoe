from Board import Board
import math
import numpy


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
                    end, victor = board.check_end()
                    if end:
                        if victor == 1:
                            print("X wins!")
                        elif victor == 2:
                            print("O wins!")
                        else:
                            print("Tie!")
                        board.print_board()
                        playing = False
            except ValueError:
                print("Not a valid input. Please try again.")

    else:
        print("You go first.")
        while playing:
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
                        end, victor = board.check_end()
                        if end:
                            if victor == 1:
                                print("X wins!")
                            elif victor == 2:
                                print("O wins!")
                            else:
                                print("Tie!")
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
                    end, victor = board.check_end()
                    if end:
                        if victor == 1:
                            print("X wins!")
                        elif victor == 2:
                            print("O wins!")
                        else:
                            print("Tie!")
                        board.print_board()
                        playing = False


def AlphaBetaSearch(state): # return action as tuple coordinates
    v, action = MAXVAL(state, -math.inf, math.inf, 0)
    # actions = Actions(state)
    # need to find which action has value v
    return action

def Actions(state):
    #return a list of legal moves
    actions = []
    for i in range(3):
        for j in range(3):
            if state.layout[i, j] == 0:
                actions.append((i, j))

    return actions

def MAXVAL(state, alpha, beta, depth):
    if CUTOFF(state, depth):
        return EVAL(state), state.lastmove
    depth += 1
    v = -math.inf
    action = (-1, -1)
    for a in Actions(state):  #figure out if iterating through keys or values
        minval, z = MINVAL(RESULT(state, a, 'O'), alpha, beta, depth)
        if v < minval:
            v = minval
            action = a
        #v = max(v, MINVAL(RESULT(state, a), alpha, beta, lastmove))
        if v >= beta:
            return v, a
        alpha = max(alpha, v)
    return v, action

def MINVAL(state, alpha, beta, depth):
    if CUTOFF(state, depth):
        return EVAL(state), state.lastmove
    v = math.inf
    depth += 1
    action = (-1, -1)
    for a in Actions(state):
        maxval, z = MAXVAL(RESULT(state, a, 'X'), alpha, beta, depth)
        # v = min(v, MAXVAL(RESULT(state, a), alpha, beta, lastmove))
        if v > maxval:
            v = maxval
            action = a
        if v <= alpha:
            return v, a
        beta = min(beta, v)
    return v, action


def EVAL(state):
    # evaluate state either victory or not if terminal or heuristic if not\
    end, victor = state.check_end()
    if end:
        if victor == 1:
            return -1000
        elif victor == 2:
            return 100
        else:
            return 0
    else:
        eval = numpy.zeros(8) # in the end will have the evaluations for [row 1, 2, 3, col 1, 2, 3,  diagonal 1, 2]
        val = 0
        for i in range(3):
            for j in range(3):
                if state[i,j] == 1:
                    val = 1
                elif state[i, j] ==2:
                    val = -1
                eval[i] += val
                eval[i+3] += val
                if i == j:
                    eval[6] += val
                elif (i, j) in {(0, 2), (1, 1), (2, 0)}:
                    eval[7] += val
        return sum(eval)

def CUTOFF(state, depth):
    end, victor = state.check_end()
    if depth >= 10 or end:
        return True
    return False

def RESULT(state, action, symbol):
    # show the result of the action on the state)
    newstate = state.copy() #copy of state and then perform action but don't copy reference
    newstate.insert(action, symbol)
    return newstate



game()