import random
from gutil import save_game, load_game, print_board

# Initialize the game board
ROWS = 6
COLUMNS = 7
board = [[' ' for _ in range(COLUMNS)] for _ in range(ROWS)]

def is_valid_move(board, col):
    return board[0][col] == ' '

def make_move(board, col, disc):
    for row in reversed(board):
        if row[col] == ' ':
            row[col] = disc
            return

def check_winner(board, disc):
    # Check horizontal locations
    for row in range(ROWS):
        for col in range(COLUMNS - 3):
            if all(board[row][col + i] == disc for i in range(4)):
                return True

    # Check vertical locations
    for col in range(COLUMNS):
        for row in range(ROWS - 3):
            if all(board[row + i][col] == disc for i in range(4)):
                return True

    # Check positively sloped diagonals
    for row in range(ROWS - 3):
        for col in range(COLUMNS - 3):
            if all(board[row + i][col + i] == disc for i in range(4)):
                return True

    # Check negatively sloped diagonals
    for row in range(3, ROWS):
        for col in range(COLUMNS - 3):
            if all(board[row - i][col + i] == disc for i in range(4)):
                return True

    return False

def is_draw(board):
    return all(board[0][col] != ' ' for col in range(COLUMNS))

def computer_move(board, disc):
    valid_moves = [col for col in range(COLUMNS) if is_valid_move(board, col)]
    col = random.choice(valid_moves)
    make_move(board, col, disc)

def play_game():
    global board
    choice = input("Choose: 1 to start a new game, 2 to load a saved game: ")
    if choice == '2':
        filename = input("Enter the filename to load: ")
        turn, mode = load_game(filename)  # Pass the filename argument here
    else:
        mode = input("Choose game mode: 1 for Player vs Player, 2 for Player vs Computer: ")
        turn = 0

    while True:
        print_board(board, COLUMNS)
        if mode == '2' and turn % 2 == 1:
            print("Computer's turn")
            computer_move(board, 'O')
        else:
            action = input(f"Player {turn % 2 + 1} ({'X' if turn % 2 == 0 else 'O'}), choose a column (0-{COLUMNS-1}) or 's' to save: ")
            if action == 's':
                filename = input("Enter the filename to save the game: ")
                save_game(board, turn, mode, filename)
                continue
            col = int(action)
            if is_valid_move(board, col):
                make_move(board, col, 'X' if turn % 2 == 0 else 'O')
            else:
                print("Invalid move. Try again.")
                continue

        if check_winner(board, 'X' if turn % 2 == 0 else 'O'):
            print_board(board, COLUMNS)
            print(f"Player {turn % 2 + 1} wins!")
            break
        if is_draw(board):
            print_board(board, COLUMNS)
            print("The game is a draw!")
            break
        turn += 1

if __name__ == "__main__":
    play_game()
