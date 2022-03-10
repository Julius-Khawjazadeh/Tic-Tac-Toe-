board = { 
    '7': ' ', '8': ' ', '9': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '1': ' ', '2': ' ', '3': ' ',
}

def printBoard(b):
    print(b['7'] + '|' + b['8'] + '|' + b['9'])
    print('-+-+-')
    print(b['4'] + '|' + b['5'] + '|' + b['6'])
    print('-+-+-')
    print(b['1'] + '|' + b['2'] + '|' + b['3'])

def game():
    counter = 0
    turn = 'X' 

    # The main game loop
    for i in range(10):
        printBoard(board)
        move = input("It's you're turn, " + turn + ". Please pick a slot from 1-9: ")

        if board[move] == ' ': # Checking to see if the selected slot is empty
            board[move] = turn
            counter += 1 
        else:
            print("That slot is already filled. Please try again: ")
            continue

        # Switching turns
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        
        print("\n")


game()
