board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
         'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
         'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(f" {board['top-L']} | {board['top-M']} | {board['top-R']}")
    print("---+---+---")
    print(f" {board['mid-L']} | {board['mid-M']} | {board['mid-R']}")
    print("---+---+---")
    print(f" {board['low-L']} | {board['low-M']} | {board['low-R']}")

turn = 'X'

for i in range(9):
    printBoard(board)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    board[move] = turn
    if turn == 'X':
         turn = 'O'
    else:
         turn = 'X'
printBoard(board)