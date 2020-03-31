import numpy as np
import random as r
board = np.array([['_', '_', '_'], ['_', '_', '_'], [' ', ' ', ' ']])
#making the array to mix with the board display type

p1s = 'X'
p2s = 'O'
c1s = 'X'
c2s = 'O'
#giving players their symbols


def display():
    print()
    print("_", str(board[0][0]), "_|_", str(
        board[0][1]), "_|_", str(board[0][2]), "_")
    print('_', str(board[1][0]), "_|_", str(
        board[1][1]), "_|_", str(board[1][2]), "_")
    print(" ", str(board[2][0]), " | ", str(
        board[2][1]), " | ", str(board[2][2]), " ")
    print()
# making the board

def c_row(symbol):
    for i in range(0, 3):
        count = 0
        for j in range(0, 3):
            if board[i][j] == symbol:
                count += 1
        if count == 3:
            print(symbol, " has won the game")
            return True
    return False
#check row for board with symbol and printing winning symbol

def c_col(symbol):
    for i in range(0, 3):
        count = 0
        for j in range(0, 3):
            if board[j][i] == symbol:
                count += 1
        if count == 3:
            print(symbol, " has won the game")
            return True
    return False
#check column for board with symbol and printing winning symbol

def c_diag(symbol):
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] == symbol) or (board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] == symbol):
        print(symbol, "Has won the match")
        return True
    return False
#check diagonal for board with symbol and printing winning symbol

def winner(symbol):
    return c_row(symbol) or c_col(symbol) or c_diag(symbol)
#returns with winning symbol

def move(symbol):
    display()
    while(1):
        row = int(input("Enter the Row address(1,2 or 3): "))
        col = int(input("Enter the column address(1,2 or 3): "))
        if (row > 0 and row < 4 and col > 0 and col < 4) and (board[row-1][col-1] == '_' or board[row-1][col-1] == ' '):
            break
        else:
            print("Invalid move detected please try again.")
    board[row - 1][col-1] = symbol
#taking the row and column inout and assigning respective symbol

def move_com(symbol):
    display()
    while(1):
        row = r.randint(0,2)
        col = r.randint(0,2)
        if (row >= 0 and row <=2 and col >= 0 and col <= 2) and (board[row][col] == '_' or board[row][col] == ' '):
            break
        else:
            print("Invalid move detected please try again.")
    board[row][col] = symbol
#making the move system for computer

def play():
    choice = input("Hello and Welcome to the game of TIC-TAC-TOE made by FUNKY_doc@69\nChoose the game mode:\n1. Player vs Player\n2. Player Vs. Computer\n3. Computer Vs Computer\nselection: ")
    choice = int(choice)
    if choice == 1:
        for turn in range(9):
            if turn % 2 == 0:
                print("Player 1's turn:\n")
                move(p1s)
                if winner(p1s):
                    break
            else:
                print("Player 2's turn:\n")
                move(p2s)
                if winner(p2s):
                    break
        if not winner(p1s) and not winner(p2s):
            print("It was a Draw")  
#player vs player

    elif choice == 2:
        for turn in range(9):
            if turn % 2 == 0:
                print("\nPlayer make your move:\n")
                move(p1s)
                if winner(p1s):
                    break
                
            else:
                print("\nComputer is making a move\n")
                move_com(c2s)
                if winner(c2s):
                    break
        if not winner(p1s) and not winner(c2s):
            print("It was a Draw")          
#player vs computer
            
    elif choice == 3:
        for turn in range(9):
            if turn % 2 == 0:
                print("\nComputer 1 make your move:\n")
                move_com(c1s)
                if winner(c1s):
                    break
                
            else:
                print("\nComputer 2 is making a move\n")
                move_com(c2s)
                if winner(c2s):
                    break
        if not winner(c1s) and not winner(c2s):
            print("It was a Draw")        
#computer vs computer
                
    else:
        print("\n!!!!Invalid input detected destroying process!!!!\n")
                
                    
#main playing function

play()
display()
#show the steps after completion

