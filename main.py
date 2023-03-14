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


def evaluate(board):
    """Evaluate the current state of the board."""
    return board[6] - board[13]  # difference between player's Kalaha and opponent's Kalaha

def generate_moves(board):
    """Generate all possible moves for the current player."""
    moves = []
    for i in range(6):
        if board[i] != 0:
            moves.append(i)
    return moves

def apply_move(board, move):
    """Apply the selected move to the current state of the game."""
    player = board[14]  # current player
    nextBoard = board.copy()
    seeds = nextBoard[move]
    nextBoard[move] = 0
    i = move + 1
    while seeds > 0:
        if i == 13 and player == 0:
            i = 0
        elif i == 6 and player == 1:
            i = 7
        nextBoard[i] += 1
        seeds -= 1
        i = (i + 1) % 14
    if i == 6 and player == 0:  # last seed lands in player's Kalaha
        nextBoard[6] += 1
    elif i == 13 and player == 1:  # last seed lands in opponent's Kalaha
        nextBoard[13] += 1
    elif nextBoard[i] == 1 and ((i < 6 and player == 0) or (i > 6 and i < 13 and player == 1)):
        # last seed lands in an empty pit on player's side
        opposite = 12 - i
        nextBoard[player * 7 + 6] += nextBoard[opposite] + 1
        nextBoard[opposite] = 0
    nextBoard[14] = 1 - player  # switch player
    return nextBoard

def minimax(board, depth, maximizingPlayer):
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

def choose_move(board, depth):
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

# Example usage
state = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0, 0]  # starting state
print("Current state:", state)
move = choose_move(state, 3)
print("Best move:", move)
nextState = apply_move(state, move)
print("Next state:", nextState)
