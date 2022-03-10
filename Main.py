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

def printResult(board, turn):
    printBoard(board)
    print("\nGame Over.")
    print("---------------------")
    print("*** Player " + turn + " won! ***\n") 

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

        # Checking to see if a player has won
        if board['7'] == board['8'] == board['9'] != ' ': # Across the top
            printResult(board, turn)
            break
        elif board['4'] == board['5'] == board['6'] != ' ': # Across the middle
            printResult(board, turn)
            break
        elif board['1'] == board['2'] == board['3'] != ' ': # Across the bottom
            printResult(board, turn)
            break
        elif board['7'] == board['4'] == board['1'] != ' ': # Down the left side
            printResult(board, turn)
            break
        elif board['8'] == board['5'] == board['2'] != ' ': # Down the middle 
            printResult(board, turn)
            break
        elif board['9'] == board['6'] == board['3'] != ' ': # Down the right side 
            printResult(board, turn)
            break
        elif board['1'] == board['5'] == board['9'] != ' ': # Diagonal 
            printResult(board, turn)
            break
        elif board['7'] == board['5'] == board['3'] != ' ': # Diagonal 
            printResult(board, turn)
            break
            
        if counter == 9: # It's a tie!
            print("\nGame Over.")
            print("---------------------")
            print("The game is a tie!")
            break 



        # Switching turns
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        
        print("\n")


game()
