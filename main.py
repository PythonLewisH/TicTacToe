import re

tic_tac_toe_board = [["|1|", "|2|", "|3|"],
                     ["|4|", "|5|", "|6|"],
                     ["|7|", "|8|", "|9|"]]

# Sets a global variable to switch off if there is a result
continue_play = True

draw = False

# Keeps a track of previous guesses so that players don't guess same square
previous_guesses = []


# Prints the board in a legible format in the console
def board(game_board):
    for i in game_board:
        for j in i:
            print(j, end=" ")
        print()


# Cycles through the list of lists (the game board) - if a players selection match a square it changes it to a
# 'X'.
def mark_square_x(player_selection):
    for i in range(len(tic_tac_toe_board)):
        for j in range(len(tic_tac_toe_board[i])):
            if player_selection == (tic_tac_toe_board[i][j][1]):
                tic_tac_toe_board[i][j] = "|X|"

    board(tic_tac_toe_board)


# same function but marks square with a 'O'
def mark_square_o(player_selection):
    for i in range(len(tic_tac_toe_board)):
        for j in range(len(tic_tac_toe_board[i])):
            if player_selection == (tic_tac_toe_board[i][j][1]):
                tic_tac_toe_board[i][j] = "|O|"

    board(tic_tac_toe_board)


# Asks p1 for a guess. Checks that the user only enters a number between 1 and 9, and string is only 1 char in length.
def player_1_guess():
    p1 = input("\nPlayer 1 please select an unused square to place your 'X' (1-9) \n")
    if not re.match("^[1-9]", p1) or len(p1) > 1:
        print("Please only use numbers 1-9")
        player_1_guess()
    elif p1 in previous_guesses:
        print("Please guess an unused square")
        player_1_guess()
    else:
        mark_square_x(p1)
        previous_guesses.append(p1)


# Asks p2 for a guess
def player_2_guess():
    p2 = input("\nPlayer 2 please select an unused square to place your 'O' (1-9) \n")
    if not re.match("^[1-9]", p2) or len(p2) > 1:
        print("Please only use numbers 1-9")
        player_2_guess()
    elif p2 in previous_guesses:
        print("Please guess an unused square")
        player_2_guess()
    else:
        mark_square_o(p2)
        previous_guesses.append(p2)


# Checks the results. Checks if draw first (if all previous guesses have been taken up on the board). Works out if
# theres a lne by looking at the combinations of X's and 0's on board. I'm sure there's a more elegant solution here
# if I wanted to spend more time...
def check_result(latest_board):
    global continue_play, draw
    if sorted(previous_guesses) == ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        continue_play = False
        draw = True
    else:
        win1 = ["|X|", "|X|", "|X|"]
        win2 = ["|O|", "|O|", "|O|"]
        x = "|X|"
        o = "|O|"
        for i in latest_board:
            if i == win1 or i == win2:
                continue_play = False
            elif latest_board[0][0] == x and latest_board[1][0] == x and latest_board[2][0] == x:
                continue_play = False
            elif latest_board[0][1] == x and latest_board[1][1] == x and latest_board[2][1] == x:
                continue_play = False
            elif latest_board[0][2] == x and latest_board[1][2] == x and latest_board[2][2] == x:
                continue_play = False
            elif latest_board[0][0] == o and latest_board[1][0] == o and latest_board[2][0] == x:
                continue_play = False
            elif latest_board[0][1] == o and latest_board[1][1] == o and latest_board[2][1] == o:
                continue_play = False
            elif latest_board[0][2] == o and latest_board[1][2] == o and latest_board[2][2] == o:
                continue_play = False
            elif latest_board[0][0] == x and latest_board[1][1] == x and latest_board[2][2] == x:
                continue_play = False
            elif latest_board[0][2] == x and latest_board[1][1] == x and latest_board[2][0] == x:
                continue_play = False
            elif latest_board[0][0] == o and latest_board[1][1] == o and latest_board[2][2] == o:
                continue_play = False
            elif latest_board[0][2] == o and latest_board[1][1] == o and latest_board[2][0] == o:
                continue_play = False
            else:
                return


# While loop that keeps players taking turns until there is a winner.
board(tic_tac_toe_board)
while continue_play:
    player_1_guess()
    check_result(tic_tac_toe_board)
    if not continue_play:
        if draw:
            print("\nGame is a draw!")
            break
        else:
            print("\nPlayer 1 Wins! \n")
            break
    else:
        player_2_guess()
        check_result(tic_tac_toe_board)
        if not continue_play:
            if draw:
                print("Game is a draw!")
                break
            else:
                print("\nPlayer 2 wins\n")
                break
