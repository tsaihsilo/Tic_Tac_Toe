import pprint

theBoard = {'top-L': 'O', 'top-M': 'X', 'top-R': 'O', 'mid-L': 'X', 'mid-M': 'O', 'mid-R': 'X', 'low-L': 'O', 'low-M': 'X', 'low-R': 'O'}

pprint.pprint(theBoard)

print()

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

print(printBoard(theBoard))
