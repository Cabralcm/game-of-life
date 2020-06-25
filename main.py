# Build a data structure to store the board state
# "Pretty-print" the board to the terminal
# Given a starting board state, calculate the next one
# Run the game forever

# Extensions - Save interesting starting positions to files, and add the ability to reload them into your Life
# Improve the user interface
# Change the rules of Life

# TO-DO
# 

TGREEN = '\033[32m' #Green text
TWHITE = '\033[37m' #White text
ENDC = '\033[m' # reset text colour to the defaults

print(TGREEN + "This is green" + ENDC)

import random

def random_state(width, height):
    board_state = [[random.randint(0,1) for i in  range(width)] for j in range(height)]  
    return board_state

def random_state2(width, height, threshold=0.5):
    board_state = [[0 if random.random() >threshold else 1 for i in range(width) ] for j in range(height)]
    return board_state

def dead_state(width,height):
    board_state = [[0 for i in range(width)] for j in range(height)]  
    return board_state

def render(board):
    out_string = ""
    height = len(board)
    width = len(board[0])
    for i in range(height):
        out_string += "|"
        for j in range(width):
            if board[i][j] == 0:
                out_string += " "
            else:
                out_string += TGREEN + "#" + ENDC
        out_string += "|\n"
    print(out_string)


def find_state(current, count):  
    if current == 1 and count <=1:
        return 0
    elif current == 1 and count<=3:
        return 1
    elif current == 1 and count >3:
        return 0
    elif current == 0 and count == 3:
        return 1
    else:
        return 0


def next_board_state(board):
    height = len(board) 
    width = len(board[0])
    
    out_board = [[None for i in range(width)] for j in range(height)]

    # Only compute inner region
    for i in range(1,height-1):
        for j in range(1,width-1):
            count = sum( [ board[i-1][j-1], board[i][j-1], board[i+1][j-1], board[i-1][j], board[i+1][j], board[i-1][j+1], board[i][j+1], board[i+1][j+1]])
            out_board[i][j] = find_state(board[i][j], count)
    
    #First and Last Row
    for i in range(0,height,height-1): #First and last row 
        for j in range(1,width-1):
            if i == 0: #First Row
                print(height)
                print(width)
                print( f"Row:{i}, Col:{j}" )
                count = sum([ board[i][j-1], board[i][j+1], board[i+1][j] ])#, board[i+1][j-1], board[i+1][j+1] ])
            else: #Last Row
                count = sum([board[i][j-1], board[i-1][j], board[i][j+1], board[i-1][j-1], board[i-1][j+1]])
            out_board = find_state(board[i][j], count)

    #First and Last Column
    for i in range(1,height-1): #Down the Row
        for j in range(0,width, width-1): #First and Last column
            if i == 1:
                count = sum([board[i][j-1], board[i+1][j], board[x][j+1], board[x+1][j-1], board[x+1][j+1] ])    
            else:
                count = sum([board[i][j-1], board[x][j+1], board[x-1][j], board[x-1][j-1], board[x-1][j+1]])
            out_board = find_state(board[i][j], count)
    
    #Corners
    for i in range(0,height, height-1): #Top and Bottom 
        for j in range(0,width,width-1): #Left and Right
            if i == 0 and j == 0: #Top Right
                count = sum([board[i+1][j], board[i][j+1], board[i+1][y+1]])
            elif i == 0 and j >0: #Top Left
                count = sum([board[i-1][j], board[i-1][j+1], board[i][j+1]])
            elif i >0 and j == 0: #Bottom Left
                count = sum([board[i][j-1], board[i+1][j], board[i+1][j-1]])
            else: #Bottom Right
                count = sum([board[i-1][j], board[i][j-1], board[i-1][j-1]])
            out_board = find_state(board[i][j], count)
    
    return out_board

             



    

####################################################################################################
# Test
####################################################################################################

def main():
    height = 5
    width = 5
    # print(dead_state(height,width, 0.1))
    board = random_state2(height, width, 0.1)


    # print(board)
    render(board)
    board = next_board_state(board)
    render(board)
    print("Done")


if __name__ =="__main__":
    main()


