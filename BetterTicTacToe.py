import random

# Initialize the board


def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]


# Display the board
def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


# Check if the board is full
def is_board_full(board):
    return all(cell != " " for row in board for cell in row)


# Check if a player has won
def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


# Get a list of empty cells
def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]


# AI move using Minimax algorithm with adjustable depth
def ai_move(board, player, depth=0):
    if player == 'O':
        best_eval = float('-inf')
        best_move = None  # Initialize the best move

        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            eval = minimax(board, 'X', depth + 1)
            board[i][j] = ' '

            if eval > best_eval:
                best_eval = eval
                best_move = (i, j)  # Store the best move

        return best_move  # Return the best move as a tuple

    else:
        best_eval = float('inf')
        best_move = None  # Initialize the best move

        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            eval = minimax(board, 'O', depth + 1)
            board[i][j] = ' '

            if eval < best_eval:
                best_eval = eval
                best_move = (i, j)  # Store the best move

        return best_move  # Return the best move as a tuple


# Minimax function to decide AI best move
def minimax(board, player, depth):
    if check_win(board, 'X'):
        return -10 + depth
    elif check_win(board, 'O'):
        return 10 - depth
    elif is_board_full(board):
        return 0

    if player == 'O':
        max_eval = float('-inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            eval = minimax(board, 'X', depth + 1)
            board[i][j] = ' '
            max_eval = max(max_eval, eval)
        return max_eval

    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            eval = minimax(board, 'O', depth + 1)
            board[i][j] = ' '
            min_eval = min(min_eval, eval)
        return min_eval


# Get user input for a valid move
def get_user_move(board):
    while True:
        try:
            row = int(input("Enter the row (1-3): ")) - 1
            col = int(input("Enter the column (1-3): ")) - 1
            if row in range(3) and col in range(3) and board[row][col] == " ":
                return row, col
            else:
                print("Invalid move. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Try again.")


# Main game loop
def main():
    print("Welcome to Tic Tac Toe!")
    while True:
        board = initialize_board()
        display_board(board)

        while True:
            user_row, user_col = get_user_move(board)
            board[user_row][user_col] = 'X'
            display_board(board)

            if check_win(board, 'X'):
                print("You win!")
                break

            if is_board_full(board):
                print("It's a draw!")
                break

            print("AI's move...")
            ai_move_result = ai_move(board, 'O', depth=0)
            board[ai_move_result[0]][ai_move_result[1]] = 'O'
            display_board(board)

            if check_win(board, 'O'):
                print("AI wins!")
                break

            if is_board_full(board):
                print("It's a draw!")
                break

        play_again = input("Play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break


if __name__ == "__main__":
    main()
