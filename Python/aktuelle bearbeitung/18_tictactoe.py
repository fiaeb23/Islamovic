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
    for reihe in board:
        if len(set(reihe)) == 1 and reihe[0] is not None:
            return reihe[0]
    return None


def check_spalte(board):
    for i in range(3):
        spalte = [board[0][i], board[1][i], board[2][i]]
        if len(set(spalte)) == 1 and None not in spalte:
            return spalte[0]
    return None

def check_diagonals(board):
    if all(board[i][i] == board[0][0] for i in range(len(board))):
        return board[0][0]
    if all(board[i][len(board)-i-1] == board[0][len(board)-1] for i in range(len(board))):
        return board[0][len(board)-1]
    return None


def check_winner(board):
    winner = check_reihes(board) or check_spalte(board) or check_diagonals(board)
    if winner:
        return winner
    return None



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
        winner = check_winner(board)
        if winner:
            print(f"{winner} wins!")
            return
        current_player = (current_player + 1) % 2


play_game()


