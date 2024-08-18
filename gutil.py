import json

def print_board(board, columns):
    for row in board:
        print('|'.join(row))
        print('-' * (2 * columns - 1))


def save_game(board, turn, mode, filename):
    game_state = {
        "board": board,
        "turn": turn,
        "mode": mode
    }
    with open(filename, 'w') as file:
        json.dump(game_state, file)
    print(f"Game saved successfully as {filename}.")

def load_game(filename):
    global board
    with open(filename, 'r') as file:
        game_state = json.load(file)
    board = game_state["board"]
    print(f"Game loaded successfully as {filename}.")
    return game_state["turn"], game_state["mode"]
