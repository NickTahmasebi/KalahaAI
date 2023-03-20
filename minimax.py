import main

board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

def checkBestMove(player, hole):
    if (main.is_game_over() == False):
        i = 1
        j = 1
        sum = 0
        if (main.is_valid_move(player, hole) == True):
            i = i+1
            return player, hole
    else:
        return player.sum

def minimax(depth, state, checkBestMove, player):
    global stateSum, stateSum1
    player = 1
    depth = 6
    if (player == 1 & depth > 0):
        while (depth < 6):
            checkBestMove()
            depth = depth-1
            moveScore()

    elif (player == 2 & depth > 0):
        while (depth < 6):
            checkBestMove()
            depth = depth-1
            moveScore(int, player)
    return True


def moveScore(int, player):
    if player == 1:

        sum.player1 - sum.player2
        return
    else:

        sum.player2 - sum.player1
        return False