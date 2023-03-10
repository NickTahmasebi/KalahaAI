# Mancala game implementation in Python

# Initialize the game board
board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

# Function to print the board
def print_board():
    print("   ", end="")
    for i in range(12, 6, -1):
        print("{:2d}".format(board[i]), end="")
    print("\n{:2d}".format(board[13]), " "*23, "{:2d}".format(board[6]))
    print("   ", end="")
    for i in range(0, 6):
        print("{:2d}".format(board[i]), end="")
    print("\n")

# Function to check if a move is valid
def is_valid_move(player, hole):
    if player == 1 and hole < 6 and board[hole] != 0:
        return True
    elif player == 2 and hole > 6 and hole < 13 and board[hole] != 0:
        return True
    else:
        return False

# Function to make a move
def make_move(player, hole):
    stones = board[hole]
    board[hole] = 0
    while stones > 0:
        hole = (hole + 1) % 14
        if player == 1 and hole == 13:
            continue
        if player == 2 and hole == 6:
            continue
        board[hole] += 1
        stones -= 1
    if player == 1 and hole < 6 and board[hole] == 1:
        board[6] += board[12 - hole] + 1
        board[12 - hole] = 0
        board[hole] = 0
    elif player == 2 and hole > 6 and hole < 13 and board[hole] == 1:
        board[13] += board[12 - hole] + 1
        board[12 - hole] = 0
        board[hole] = 0

# Function to check if the game is over
def is_game_over():
    if sum(board[0:6]) == 0 or sum(board[7:13]) == 0:
        return True
    else:
        return False

# Function to determine the winner
def determine_winner():
    if board[6] > board[13]:
        print("Player 1 wins!")
    elif board[6] < board[13]:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

# Main game loop
player = 1
while not is_game_over():
    print_board()
    hole = int(input("Player " + str(player) + ", choose a hole (0-5 or 7-12): "))
    if is_valid_move(player, hole):
        make_move(player, hole)
        if player == 1:
            player = 2
        else:
            player = 1
    else:
        print("Invalid move. Please try again. ")
print_board()
determine_winner()
