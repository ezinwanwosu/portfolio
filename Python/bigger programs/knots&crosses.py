#This program is a game of Knots and crosses against the computer
def printboard():
    ''' This prints the board '''
    board = [[f' |' for i in range(3)] for j in range(3)]
    return board
def GetRowColumn():
    ''' This gets the row and column from the user '''
    valid = False
    while valid == False:
        try:
            column = int(input("Enter a column: "))
            row = int(input("Enter a row: "))
            if (column >= 0 and column <= 2) and (row >= 0 and row <= 2):
                valid = True
            else:
                valid = False
        except:
            print('Enter integer' )
            valid = False
    return row,column
def PlayerMove(board):
    valid = False
    while valid == False:
        row,column = GetRowColumn()
        if board[row][column] != 'x|' and board[row][column] !=  'o|':
            board[row][column] = 'x|'
            win = checkWin(board,row,column)
            
            valid = True
        else:
            print("This space is already occupied. Try again.")
            valid = False
    return win
def ComputerMove(board):
    import random as r
    valid = False
    row = r.randint(0,2)
    col = r.randint(0,2)
    
    while valid == False:
        if board[row][col] != 'x|' and board[row][col] !=  'o|':
            board[row][col] = 'o|'
            win = checkWin(board,row,col)
            valid = True
        else:
            row = r.randint(0,2)
            col = r.randint(0,2)
    return win
      
def checkWin(board,row,column):
    win = True
    if board[row][column] == 'x|':
        winner = 'Player'
    else:
        winner = 'Computer'
    
    if board[row][column] == board[row-1][column] == board[row-2][column]:
        print(winner, ' wins')
    elif board[row][column] == board[row][column-1] == board[row][column-2]:
        print(winner,' wins')
    elif board[0][0] == board[1][1] == board[2][2] != ' |':
        
        print(winner,' wins')
    elif board[2][0] == board[1][1] == board[0][2] != ' |':
        #print(board[row-2][column],board[row-1][column-1],board[row][column-2])
        if board[2][0] == 'x|':
            winner = 'Player'
        else:
            winner = 'Computer'
        print(winner,' wins')
    else:
        win = False
    

  
    return win
def endgame(board):
    end = 0
    endGame = False
    for i in range(3):
        for j in range(3):
            if board[i][j] == ('|x|' or '|o|'):
                end += 1
            else:
                pass
    if end == 9:
        endGame = True
    return endGame        
def main():
    
    board = printboard()
    for i in board:
        print(' '.join(i))
    endGame = endgame(board)
    while endGame == False:
        print('PLAYER TURN')
        win = PlayerMove(board)
        print(win)
        for i in board:
            print(' '.join(i))
        if win == True:
            break
        else:
            pass
        
        print('COMPUTER TURN')
        win = ComputerMove(board)
        
        for i in board:
            print(' '.join(i))
        if win == True:
            break
main()

