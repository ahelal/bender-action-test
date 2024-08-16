import random
import json
from game import ROWS, COLUMNS, check_winner, is_draw, print_board

def test_play_game():
    # Test case 1: Player vs Player, Player 1 wins
    board = [[' ' for _ in range(COLUMNS)] for _ in range(ROWS)]
    board[5][0] = 'X'
    board[5][1] = 'O'
    board[4][0] = 'X'
    board[4][1] = 'O'
    board[3][0] = 'X'
    board[3][1] = 'O'
    board[2][0] = 'X'
    assert check_winner(board, 'X') == True

    # Test case 2: Player vs Player, Player 2 wins
    board = [[' ' for _ in range(COLUMNS)] for _ in range(ROWS)]
    board[5][0] = 'X'
    board[5][1] = 'O'
    board[4][0] = 'X'
    board[4][1] = 'O'
    board[3][0] = 'X'
    board[3][1] = 'O'
    board[2][0] = 'O'
    board[2][1] = 'O'
    assert check_winner(board, 'O') == True

    # Test case 3: Player vs Player, draw
    board = [[' ' for _ in range(COLUMNS)] for _ in range(ROWS)]
    board[5][0] = 'X'
    board[5][1] = 'O'
    board[4][0] = 'X'
    board[4][1] = 'O'
    board[3][0] = 'O'
    board[3][1] = 'X'
    board[2][0] = 'X'
    board[2][1] = 'O'
    board[1][0] = 'O'
    board[1][1] = 'X'
    board[0][0] = 'X'
    board[0][1] = 'O'
    print_board(board)
    print("board", is_draw(board))
    assert is_draw(board) == True

    # Test case 4: Player vs Computer, Player wins
    board = [[' ' for _ in range(COLUMNS)] for _ in range(ROWS)]
    board[5][0] = 'X'
    board[5][1] = 'O'
    board[4][0] = 'X'
    board[4][1] = 'O'
    board[3][0] = 'X'
    board[3][1] = 'O'
    board[2][0] = 'X'
    assert check_winner(board, 'X') == True

    # Test case 5: Player vs Computer, Computer wins
    board = [[' ' for _ in range(COLUMNS)] for _ in range(ROWS)]
    board[5][0] = 'X'
    board[5][1] = 'O'
    board[4][0] = 'X'
    board[4][1] = 'O'
    board[3][0] = 'X'
    board[3][1] = 'O'
    board[2][0] = 'O'
    board[2][1] = 'O'
    assert check_winner(board, 'O') == True

    # Test case 6: Player vs Computer, draw
    board = [[' ' for _ in range(COLUMNS)] for _ in range(ROWS)]
    board[5][0] = 'X'
    board[5][1] = 'O'
    board[4][0] = 'X'
    board[4][1] = 'O'
    board[3][0] = 'O'
    board[3][1] = 'X'
    board[2][0] = 'X'
    board[2][1] = 'O'
    board[1][0] = 'O'
    board[1][1] = 'X'
    board[0][0] = 'X'
    board[0][1] = 'O'
    assert is_draw(board) == True

test_play_game()