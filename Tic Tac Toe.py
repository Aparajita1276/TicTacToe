import random
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")
def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
def is_full(board):
    return all(cell != " " for row in board for cell in row)
def get_computer_move(board):
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    return random.choice(empty_cells)
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    human = "X"
    computer = "O"
    while True:
        print_board(board)
        try:
            row = int(input(f"Your move (row 1-3): ")) - 1
            col = int(input(f"Your move (col 1-3): ")) - 1
        except ValueError:
            print("Please enter valid numbers.")
            continue
        if not (0 <= row < 3 and 0 <= col < 3):
            print("Invalid position! Choose from 1 to 3.")
            continue
        if board[row][col] != " ":
            print("Cell already taken! Try again.")
            continue
        board[row][col] = human
        if check_winner(board, human):
            print_board(board)
            print("🎉 You win!")
            break
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break
        print("Computer's turn...")
        r, c = get_computer_move(board)
        board[r][c] = computer
        if check_winner(board, computer):
            print_board(board)
            print("💻 Computer wins!")
            break
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

tic_tac_toe()
