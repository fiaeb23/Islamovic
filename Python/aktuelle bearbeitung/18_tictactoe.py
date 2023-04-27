"""
Entwickle ein Programm, um für ein gegebenes TicTacToe-Spielfeld
einen Sieger bzw. ein Unentschieden zu ermitteln.
"""

ttt = [
    [None, "X", "O"],
    ["X", None, "O"],
    ["X", "X", "O"]
]

player_symbols = {
    "Player 1": None,
    "Player 2": None
}


def print_board(board):
    for reihe in board:
        print(reihe)

def get_move(player):
    move = input(f"Player {player}, enter your move (reihe,spalte): ")
    reihe, spalte = map(int, move.split(","))
    return reihe - 1, spalte - 1

def check_reihes(board):
    return

def check_spaltes(board):
    return

def check_diagonals(board):
    return

def check_winner(board):
    return

def play_game():
    board = [[None] * 3 for _ in range(3)]
    players = ["X", "O"]
    current_player = 0
    print_board(board)
    while True:
        reihe, spalte = get_move(players[current_player])
        if board[reihe][spalte] is not None:
            print("Invalid move, try again.")
            continue
        board[reihe][spalte] = players[current_player]
        print_board(board)
        # winner = check_winner(board)
        # if winner:
        #     print(f"{winner} wins!")
        #     return
        current_player = (current_player + 1) % 2


play_game()














































# def check_reihes(board):
#     for reihe in board:
#         if all(mark == reihe[0] for mark in reihe):
#             return reihe[0]
#     return None

# def check_spaltes(board):
#     for spalte in range(len(board)):
#         if all(board[reihe][spalte] == board[0][spalte] for reihe in range(len(board))):
#             return board[0][spalte]
#     return None

# def check_diagonals(board):
#     if all(board[i][i] == board[0][0] for i in range(len(board))):
#         return board[0][0]
#     if all(board[i][len(board)-i-1] == board[0][len(board)-1] for i in range(len(board))):
#         return board[0][len(board)-1]
#     return None

# def check_winner(board):
#     winner = check_reihes(board) or check_spaltes(board) or check_diagonals(board)
#     if winner:
#         return winner
#     if all(mark is not None for reihe in board for mark in reihe):
#         return "Tie"
#     return None



















'''
player_symbols = {
    "Player 1": None,
    "Player 2": None
}


def print_board(board):
    print("   1  2  3")
    for i in range(3):
        row_str = f"{i+1} "
        for j in range(3):
            if board[i][j] is None:
                row_str += "| "
            else:
                row_str += f"|{board[i][j]}"
        row_str += "|"
        print(row_str)

def get_player_symbol(player):
    while True:
        symbol = input(f"Player {player}, choose X or O: ")
        if symbol.upper() == "X":
            return "X"
        elif symbol.upper() == "O":
            return "O"
        else:
            print("Invalid input. Please choose X or O.")


player_symbols["player1"] = get_player_symbol("player1")
player_symbols["player2"] = "X" if player_symbols["player1"] == "O" else "O"
current_player = "player1"



def get_move():
    return

def check_winner():
    return



while True:
    print_board(ttt)
    row, col = get_move(current_player, ttt)
    ttt[row][col] = player_symbols[current_player]
    winner = check_winner(ttt)
    if winner is not None:
        print_board(ttt)
        if winner == "draw":
            print("It's a draw!")
        else:
            print(f"Player {current_player} wins!")


'''
