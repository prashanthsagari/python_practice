def clear_output():
    print('\n'*100)
def display_board(board):
    print(f'{board[7]} | {board[8]} | {board[9]}')
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print(f'{board[1]} | {board[2]} | {board[3]}')

def player_input():
    marker = ' '
    
    while marker != 'X' and marker != 'O':
        marker = input('Player 1: choose X or O : ').upper()
        
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker
    clear_output()
    display_board(board)
    
board = ['#','X','O','O','X','O','X','O','X','X']
display_board(board)
clear_output()
display_board(board)
place_marker(board, 'M', 2)


