import random

def display_board(board):
    print('',board[1],'|',board[2],'|',board[3],'\n',
          '---------','\n',
          board[4],'|',board[5],'|',board[6],'\n',
          '---------','\n',
          board[7],'|',board[8],'|',board[9])
        
    pass


def place_marker(board, marker, position):
    board[position] = marker
    
    pass

def player_input():
    player1 = input("Please pick a marker 'X' or 'O'").upper()

    
    while player1 != 'X' and player1 != 'O':
        player1 = input("Please pick a marker 'X' or 'O'").upper()
        
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    
    return player1, player2

def win_check(board, mark):
    
    win = False
    
    if board[1] == mark and board[2] == mark and board[3] == mark: win = True
    elif board[4] == mark and board[5] == mark and board[6] == mark: win = True
    elif board[7] == mark and board[8] == mark and board[9] == mark: win = True
    elif board[1] == mark and board[4] == mark and board[7] == mark: win = True
    elif board[2] == mark and board[5] == mark and board[8] == mark: win = True
    elif board[3] == mark and board[6] == mark and board[9] == mark: win = True
    elif board[1] == mark and board[5] == mark and board[9] == mark: win = True
    elif board[3] == mark and board[5] == mark and board[7] == mark: win = True
            
    return win

def choose_first():
    firstplayer = random.randint(1,2)
    print('first player is player {}'.format(firstplayer))
    
    return firstplayer

def space_check(board, position):
    
    return (board[position] == ' ')

def full_board_check(board):
    full = False
    for pos in range(1,10):
        if board[pos] == ' ':
            full = True
            break
    
    return full

def player_choice(board):
    
    
    while True:
        try:
            position = int(input("Please pick a position 1 to 9:"))
      
            if position not in range(1,10):
               
                print("Out of range. Try again")
                continue
                
            if space_check(board,position) == False:
                print("Position taken.  Try again")
                continue
            
            break
        except ValueError:
            print("Not a valid number. Try again")
            
    print("You chose position {}".format(position))
    
    return position

def game_on():
    
    print('Welcome to Tic Tac Toe!')

    game_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    display_board(game_board)

    marker1, marker2 = player_input()
    
    print('player one is {}'.format(marker1))
    print('player two is {}'.format(marker2))
    
    nextplayer = choose_first()
    
    while full_board_check(game_board):
        
        player = nextplayer
        if player == 1:
            marker = marker1
        else:
            marker = marker2
        print("ok player {} your turn".format(player))
        print("place your {}".format(marker))
        
        chosen_position = player_choice(game_board)
    
        if space_check(game_board, chosen_position) == True:
            place_marker(game_board,marker,chosen_position)
            display_board(game_board)
        
        if win_check(game_board,marker) == True:
            print("player {} wins".format(player))
            break
        else:
            print("no win")
            
        if player == 1:
            nextplayer = 2
        else:
            nextplayer = 1

    print("Game over")
