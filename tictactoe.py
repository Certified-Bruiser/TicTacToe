# Create a 3x3 Tic-Tac-Toe board
board = [' ' for _ in range(9)]

# Define player symbols
player = 'X'
computer = 'O'

# Define the is_winner function
def is_winner(board, player):
    # Check for winning combinations
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Define the is_board_full function
def is_board_full(board):
    # Check if the board is full
    return ' ' not in board

# Define the print_board function
def print_board(board):
    for i in range(0, 9, 3):
        print(board[i], '|', board[i + 1], '|', board[i + 2])
        if i < 6:
            print('-' * 9)

# Define the minimax function
def minimax(board, depth, is_maximizing):
    if is_winner(board, computer):
        return 1
    if is_winner(board, player):
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == ' ':
                board[i] = computer
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == ' ':
                board[i] = player
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

# Main game loop
while True:
    print_board(board)

    move = int(input("Enter your move (0-8): "))
    if board[move] == ' ':
        board[move] = player

        if is_winner(board, player):
            print_board(board)
            print("You win!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

    # Computer's turn
    best_move = -1
    best_score = -float("inf")

    for i in range(9):
        if board[i] == ' ':
            board[i] = computer
            score = minimax(board, 0, False)
            board[i] = ' '

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = computer

    if is_winner(board, computer):
        print_board(board)
        print("Computer wins!")
        break
    elif is_board_full(board):
        print_board(board)
        print("It's a draw!")
        break
