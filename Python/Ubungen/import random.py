import random

def coin_toss():
    """Simulate a coin toss and return 'H' for heads or 'T' for tails"""
    return random.choice(['H', 'T'])

def play_game():
    """Play the coin toss game and return True if the player wins, False otherwise"""
    count = 0
    while count < 3:
        result = coin_toss()
        print(result)
        if result == 'H':
            count += 1
        else:
            count = 0
    if count == 3:
        return True
    else:
        return False

if __name__ == '__main__':
    if play_game():
        print('You won!')
    else:
        print('You lost!')
