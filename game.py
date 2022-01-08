def display_board(board):
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

def player_input():
    marker = ''
    while marker != 'X' and marker !='O':
        marker = input('Please choose if you want to be X or O')
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return (board[1] == board[2] == board[3] == mark or
    board[4] == board[5] == board[6] == mark or
    board[7] == board[8] == board[9] == mark or
    board[1] == board[4] == board[7] == mark or
    board[2] == board[5] == board[8] == mark or
    board[3] == board[6] == board[9] == mark or
    board[1] == board[5] == board[9] == mark or
    board[3] == board[5] == board[7] == mark)

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in range(1,10) or not space_check(board,position):
        position = int(input('Choose a position (1-9): '))
    return position

def replay():
    choice = input('Play again? Enter Yes or No:')
    return choice == 'Yes'

print('Welcome to the Tic Tac Toe')

while True:
    theBoard = [' ']*10
    player1Marker ,player2Marker = player_input()
    turn = 'Player 1'
    print(turn + " will go first.")

    play_game = input('Ready to play? y or n: ')
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'Player 1':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1Marker, position)
            if win_check(theBoard,player1Marker):
                display_board(theBoard)
                print('Player1 has won.')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("This is a TIE.")
                    break
                else:
                    turn = 'Player 2'
        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2Marker, position)
            if win_check(theBoard,player2Marker):
                display_board(theBoard)
                print('Player2 has won.')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("This is a TIE.")
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break