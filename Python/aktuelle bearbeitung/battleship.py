import random

# Create the game board
board = []
board_size = 5

for _ in range(board_size):
    board.append(["O"] * board_size)

# Place the battleship randomly on the board
ship_row = random.randint(0, board_size - 1)
ship_col = random.randint(0, board_size - 1)

# Game loop
for turn in range(4):  # Four turns to guess the battleship's location
    print(f"Turn {turn + 1}")
    
    # Get the player's guess
    guess_row = int(input("Guess Row (0-4): "))
    guess_col = int(input("Guess Col (0-4): "))

    # Check if the guess is correct
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        break
    else:
        # Check if the guess is within the board
        if guess_row not in range(board_size) or guess_col not in range(board_size):
            print("Oops, that's not even in the ocean.")
        # Check if the guess was already made
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"

        # Print the current state of the board
        for row in board:
            print(" ".join(row))
    
    # End of the game
    if turn == 3:
        print("Game Over")
        print(f"The battleship was at row {ship_row} and column {ship_col}.")
