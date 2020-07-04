from Board.py import Board


def game():
    single_player = False
    players = input("Please input 1 or 2 players.")
    if players == "1":
        print("You have selected single-player mode.")
        single_player = True
    elif players != "2":
        print("That was not one of the options. You have been defaulted to 2 player mode.")
    else:
        print("You have selected 2 player mode.")

    board = Board()
    example_board = "    |     |    \n" \
                    "  "+{}+"  |  "+{}+"  |  "+{}+ "  \n" +\
                    "____|____|____"+ \
                    "    |     |    \n" \
                    "  " + {} + "  |  " + {} + "  |  " + {} + "  \n" + \
                    "____|____|____" + \
                    "    |     |    \n" \
                    "  " + {} + "  |  " + {} + "  |  " + {} + "  \n" + \
                    "     |     |     ".format('1', '2', '3', '4', '5', '6', '7', '8', '9')
    print("When it is your turn, indicate which space you would like to use by inputting the number of that space")
    print(example_board)
    print("You may not use a space which has already been filled")
    print("The game will end when one player has filled a row or column with their symbol, or when the board is filled")
    if not single_player:
        print("X goes first")