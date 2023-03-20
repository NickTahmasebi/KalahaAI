# Mancala game implementation in Python

# Initialize the game board
board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

# Function to print the board
def print_board(): #Seb
    print("  {12}{11}{10}{9}{8}{7}\n")

    print("   ", end="")
    for i in range(12, 6, -1):
        print("{:2d} ".format(board[i]), end="")
    print("\n{:2d}".format(board[13]), " "*16, "{:2d}".format(board[6]))
    print("   ", end="")
    for i in range(0, 6):
        print("{:2d} ".format(board[i]), end="")
    print("\n")
    print("   {0}{1}{2}{3}{4}{5}")

# Function to check if a move is valid
def is_valid_move(player, hole): #Nick
    if player == 1 and hole < 6 and board[hole] != 0:
        return True
    elif player == 2 and hole > 6 and hole < 13 and board[hole] != 0:
        return True
    else:
        return False

# Function to make a move
def make_move(player, hole): #Hylle
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



# Function to check if the game is over
def is_game_over(): #Valde
    if sum(board[0:6]) == 0 or sum(board[7:13]) == 0:
        return True
    else:
        return False

# Function to determine the winner

def generate_moves(board): #Hylle
    """Generate all possible moves for the current player."""
    moves = []
    for i in range(6):
        if board[i] != 0:
            moves.append(i)
    return moves

def evaluate(board): #Seb
    """Evaluate the current state of the board."""
    return board[6] - board[13]  # difference between player's Kalaha and opponent's Kalaha


def apply_move(board, move): #Nick
    """Apply the selected move to the current state of the game."""
    player = board[13]  # current player
    nextBoard = board.copy()
    seeds = nextBoard[move]
    nextBoard[move] = 0
    i = move + 1
    while seeds > 0:
        if i == 12 and player == 0:
            i = 0
        elif i == 5 and player == 1:
            i = 7
        nextBoard[i] += 1
        seeds -= 1
        i = (i + 1) % 14
    if i == 5 and player == 0:  # last seed lands in player's Kalaha
        nextBoard[5] += 1
    elif i == 12 and player == 1:  # last seed lands in opponent's Kalaha
        nextBoard[12] += 1
    elif nextBoard[i] == 1 and ((i < 5 and player == 0) or (i > 5 and i < 12 and player == 1)):
        # last seed lands in an empty pit on player's side
        opposite = 11 - i
        nextBoard[player * 7 + 5] += nextBoard[opposite] + 1
        nextBoard[opposite] = 0
    nextBoard[13] = 1 - player  # switch player
    return nextBoard

def minimax(board, depth, maximizingPlayer): #Valde
    """Apply the minimax algorithm to determine the best move for the current player."""
    if depth == 0 or board[6] == 0 or board[13] == 0:
        return evaluate(board)
    if maximizingPlayer:
        bestValue = -float("inf")
        for move in generate_moves(board):
            nextBoard = apply_move(board, move)
            value = minimax(nextBoard, depth-1, False)
            bestValue = max(bestValue, value)
        return bestValue
    else:
        bestValue = float("inf")
        for move in generate_moves(board):
            nextBoard = apply_move(board, move)
            value = minimax(nextBoard, depth-1, True)
            bestValue = min(bestValue, value)
        return bestValue

def choose_move(board, depth): #Hylle
    """Choose the best move for the current player."""
    moves = generate_moves(board)
    bestValue = -float("inf")
    bestMove = None
    for move in moves:
        nextBoard = apply_move(board, move)
        value = minimax(nextBoard, depth-1, False)
        if value > bestValue:
            bestValue = value
            bestMove = move
    return bestMove

def determine_winner():
    if board[6] > board[13]:
        print("Player 1 wins!")
    elif board[6] < board[13]:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

def play_game():
    player = 1
    while not is_game_over():
        print_board()
        move = choose_move(board, 8)
        if(player==1):
            print("Best move:", move)
            hole = int(input("Player " + str(player) + ", choose a hole (0-5):  "))
        else:
            hole = int(input("Player " + str(player) + ", choose a hole (7-12):  "))

        if is_valid_move(player, hole):
            make_move(player, hole)
            if player == 1:
                player = 2
            else:
                player = 1
        else:
            print("Invalid move. Please try again. ")


play_game()
determine_winner()