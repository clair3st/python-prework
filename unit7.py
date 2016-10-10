from random import randint

# initialize game with board
board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

# Starting the game
print "Let's play Battleship!"
print_board(board)

# Puting the ship in a random place on the board
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# starting the game, counting turns
for turn in range(4):
    print "Turn", turn + 1
    # get the users guess
    guess_row = int(raw_input("Guess Row:")) - 1
    guess_col = int(raw_input("Guess Col:")) - 1

    # if the guess is right the game ends
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break

    else:
        # if the guess is outside the box, error message
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
            continue
        # if the guess has already been guessed, error message
        elif (board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
        # message for missed guess
            print "You missed my battleship!"
    # turn O to X to show guess
    board[guess_row][guess_col] = "X"
    # reprint board
    print_board(board)
    if turn == 3:
        print "Game Over"
