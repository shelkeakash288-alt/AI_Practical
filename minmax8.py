def winner(board):

    lines = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for a, b, c in lines:

        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    return None


def minimax(board, is_max):

    result = winner(board)

    if result == "X":
        return 1

    if result == "O":
        return -1

    if " " not in board:
        return 0

    if is_max:

        best = -float("inf")

        for i in range(9):

            if board[i] == " ":

                board[i] = "X"

                score = minimax(board, False)

                board[i] = " "

                best = max(best, score)

        return best

    else:

        best = float("inf")

        for i in range(9):

            if board[i] == " ":

                board[i] = "O"

                score = minimax(board, True)

                board[i] = " "

                best = min(best, score)

        return best


def best_move(board):

    best_score = -float("inf")

    move = None

    for i in range(9):

        if board[i] == " ":

            board[i] = "X"

            score = minimax(board, False)

            board[i] = " "

            if score > best_score:

                best_score = score
                move = i

    return move


board = [" "] * 9

move = best_move(board)

print("Tic-Tac-Toe Positions:")

print("1 | 2 | 3")
print("--+---+--")
print("4 | 5 | 6")
print("--+---+--")
print("7 | 8 | 9")

print("\nBest Move for X:", move + 1)