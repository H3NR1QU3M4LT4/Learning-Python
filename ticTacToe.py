theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def switch(arg):
    switcher= {
        1: 'top-L',
        2: 'top-M',
        3: 'top-R',
        4: 'mid-L',
        5: 'mid-M',
        6: 'mid-R',
        7: 'low-L',
        8: 'low-M',
        9: 'low-R',
    }
    return switcher.get(arg, "Invalid number!")

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    while True:
        print('Turn for ' + turn + '. Move on which space?')
        move = int(input())
        if (move < 1) or (move > 9):
            print('Try again!')
            continue
        
        theBoard[switch(move)] = turn
        printBoard(theBoard)

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        
