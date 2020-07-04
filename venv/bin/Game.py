from Board import Board


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
    if not single_player:
        print("X goes first")



        while True:
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
                        break
            except:
                print("Not a valid input. Please try again.")









game()