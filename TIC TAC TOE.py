import os
import random

def display_board(available, board):
    
    clear = lambda : os.system('cls')
    
    print('Available   TIC-TAC-TOE\n'+
           '  moves\n\n  '+
          available[7]+'|'+available[8]+'|'+available[9]+'        '+board[7]+' | '+board[8]+' | '+board[9]+'\n  '+
          '-----        -----\n  '+
          available[4]+'|'+available[5]+'|'+available[6]+'        '+board[4]+' | '+board[5]+' | '+board[6]+'\n  '+
          '-----        -----\n  '+
          available[1]+'|'+available[2]+'|'+available[3]+'        '+board[1]+' | '+board[2]+' | '+board[3]+'\n')
    


def player_input():
    maker = ''
    
    while not (maker == 'X' or maker == 'O'):
        maker = input('Player 1: Please choose your marker (X or O):').upper()
    if maker == 'X':
        return('X', 'O')
    else:
        return('O', 'X')


def place_marker(available, board, marker, position):
    board[position] = marker
    available[position] = ' '

def win_check(board, mark):
    if ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[6] == mark and board[5] == mark and board[4] == mark) or (board[1] == mark and board[2] == mark and board[3] == mark)
    or (board[1] == mark and board[4] == mark and board[7] == mark) or (board[2] == mark and board[5] == mark and board[8] == mark)
    or (board[3] == mark and board[6] == mark and board[9] == mark) or (board[1] == mark and board[5] == mark and board[9] == mark)
    or (board[3] == mark and board[5] == mark and board[7] == mark)):
        return True
    else:
        return False

def choose_first():
    chance = random.randint(1, 2)
    if chance == 1:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    
    if board[position] == '':
        return True
    else:
        return False



def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    
    next_move = 0
    while  next_move not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, next_move):
        next_move = int(input('Please enter your next move(1-9): '))
        
    return next_move


def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

print('Welcome to Tic Tac Toe!')

while True:
    the_board = ['']*10
    available = [str(num) for num in range(0, 10)]
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')
    
    play = input('Are you ready to play. (Y or N): ')
    
    if play.lower()[0] == 'y':
        game = True
    else:
        game = False
    
    while game:
        #Player 1 Turn
        if turn == 'Player 1':
            display_board(available, the_board)
            position = player_choice(the_board)
            place_marker(available, the_board, player1_marker, position)
            
            if win_check(the_board, player1_marker):
                display_board(available, the_board)
                print('******* Congratulation, Player 1 won *******')
                game = False
            else: 
                if full_board_check(the_board):
                    display_board(available, the_board)
                    print('<<< OOPS!!! The match is a draw!!!! >>>')
                    break
                else:
                    turn = 'Player 2'
        
        # Player2's turn.
        else:
            if turn == 'Player 2':
                display_board(available,the_board)
                position = player_choice(the_board)
                place_marker(available, the_board, player2_marker, position)
            
            if win_check(the_board, player2_marker):
                display_board(available, the_board)
                print('******* Congratulation, Player 2 won *******')
                game = False
            else: 
                if full_board_check(the_board):
                    display_board(available, the_board)
                    print('<<< OOPS!!! The match is a draw!!!! >>>')
                    break
                else:
                    turn = 'Player 1'
            
    if not replay():
        break