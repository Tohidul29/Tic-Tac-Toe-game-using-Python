import random

# Define the board as a list of empty strings
board = [' '] * 9

# Define the possible winning combinations
winning_combinations = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

# Define the function to print the board
def print_board():
    print('-------------')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('-------------')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('-------------')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('-------------')

# Define the function to check for a winner
def check_winner(player):
    for combo in winning_combinations:
        if board[combo[0]] == player and board[combo[1]] == player and board[combo[2]] == player:
            return True
    return False

# Define the function for the player's turn
def player_turn():
    print('Your turn!')
    position = int(input('Choose a position (1-9): '))
    if board[position - 1] != ' ':
        print('Position already taken. Try again.')
        player_turn()
    else:
        board[position - 1] = 'X'
        print_board()
        if check_winner('X'):
            print('Congratulations! You won!')
            exit()
        elif ' ' not in board:
            print('Game over! It was a tie.')
            exit()

# Define the function for the computer's turn
def computer_turn():
    print('Computer\'s turn!')
    position = random.randint(0, 8)
    if board[position] != ' ':
        computer_turn()
    else:
        board[position] = 'O'
        print_board()
        if check_winner('O'):
            print('Sorry! The computer won!')
            exit()
        elif ' ' not in board:
            print('Game over! It was a tie.')
            exit()

# Play the game!
print('Welcome to Tic Tac Toe!')
print_board()
while True:
    player_turn()
    computer_turn()
