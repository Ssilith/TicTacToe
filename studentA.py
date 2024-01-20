def new_board(): 
    return [' '] * 25


def print_board(board):
    for i in range(0, 25, 5):
        print(' | '.join(board[i:i + 5]))
        if i < 20:
            print("-----------------")
    print("\n\n")


def is_game_over(board):
    if ' ' not in board:
        return True

    for i in range(0, 25, 5):
        if board[i] != ' ' and all(board[j] == board[i] for j in range(i + 1, i + 5)):
            return True

    for i in range(5):
        if board[i] != ' ' and all(board[j] == board[i] for j in range(i + 5, 25, 5)):
            return True

    if board[0] != ' ' and all(board[i] == board[0] for i in range(6, 25, 6)):
        return True

    if board[4] != ' ' and all(board[i] == board[4] for i in range(8, 20, 4)):
        return True
    return False


def announce_outcome(board, players_move):
    if is_game_over(board):
        if ' ' not in board:
            print("It's a draw!")
        elif players_move:
            print("AI won")
        else:
            print("You won")
