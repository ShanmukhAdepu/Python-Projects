
"""
sudoko is going to be the actuall 2D array that represents the game
pos is simply the coordinates (row, col)
num is a simple number 
"""

#This part of the code is meant to solve the sudoko using backtracking"
def solve(sudoko):

    find = findEmpty(sudoko)
    if find:
        row, col = find
    else:
        return True

    for i in range(1, 10):
        
        if valid(sudoko, (row, col), i):
            sudoko[row][col] = i

            if solve(sudoko):
                return True

            sudoko[row][col] = 0

    return False

#this function should return true if the sudoko is correct and false if it is not
def valid(sudoko, pos, num):    
    
    #checks rows
    for i in range(0, len(sudoko)):
        
        if sudoko[pos[0]][i] == num and pos[1] != i:

            return False

    #checks columns
    for i in range(0, len(sudoko)):

        if sudoko[i][pos[0]] == num and pos[1] != i:

            return False
    
    #checks boxes
    xBox = pos[1]//3
    yBox = pos[0]//3

    for i in range (yBox * 3, yBox*3+3):
        
        for j in range (xBox * 3, xBox*3+3):
            
            if sudoko[i][j] == num and (i, j) != pos:
                
                return False

    return True

#finds an empty space on the board
#sudoko in this function would be partially complete
def findEmpty(sudoko):
   
    for i in range(len(sudoko)):
       
        for j in range(len(sudoko[0])):
            
            if sudoko[i][j] == 0:
               
                return (i, j)

    return None

#prints the board
def printBoard(sudoko):

    for i in range (len(sudoko)):

        if i % 3 == 0 and i != 0:

            print("- - - - - - - - - - - - - - -")
        
        for j in range(len(sudoko[0])):

            if j % 3 == 0:

                print(" | ", end ="")
            
            if j == 8:

                print(sudoko[i][j], end = "\n")
            
            else:
            
                print(str(sudoko[i][j]) + " ", end ="")


