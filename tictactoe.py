import random

# a function to draw the game board
def draw_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

# a function to choose the first player
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

# a function to determine if a space on the board is available
def space_free(board, move):
    return board[move] == ' '

# a function to add a move to the board
def make_move(board, move, symbol):
    board[move] = symbol

# a function to check if a player has won
def is_winner(board, symbol):
    return ((board[7] == symbol and board[8] == symbol and board[9] == symbol) or # top row
            (board[4] == symbol and board[5] == symbol and board[6] == symbol) or # middle row
            (board[1] == symbol and board[2] == symbol and board[3] == symbol) or # bottom row
            (board[7] == symbol and board[4] == symbol and board[1] == symbol) or # left column
            (board[8] == symbol and board[5] == symbol and board[2] == symbol) or # middle column
            (board[9] == symbol and board[6] == symbol and board[3] == symbol) or # right column
            (board[7] == symbol and board[5] == symbol and board[3] == symbol) or # diagonal
            (board[9] == symbol and board[5] == symbol and board[1] == symbol)) # diagonal

# a function to check if the board is full
def is_board_full(board):
    for i in range(1, 10):
        if space_free(board, i):
            return False
    return True

# a function to get the player's move
def get_move(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not space_free(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

# main
print('Welcome to Tic-Tac-Toe!')

while True:
    # reset the board
    the_board = [' '] * 10
    player1_symbol, player2_symbol = 'X', 'O'
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player 1's turn
            draw_board(the_board)
            move = get_move(the_board)
            make_move(the_board, move, player1_symbol)

            if is_winner(the_board, player1_symbol):
                draw_board(the_board)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player 2's turn
            draw_board(the_board)
            move = get_move(the_board)
            make_move(the_board, move, player2_symbol)

            if is_winner(the_board, player2_symbol):
                draw_board(the_board)
                print('Player 2 has won!')
                game_on = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
