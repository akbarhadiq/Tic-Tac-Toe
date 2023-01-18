# Tic Tac Toe Requirement :

# Printing the game board
# take player input
# check for win or tie

# switch the player
# take input
# check for win or tie

# Create board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# first player is always 'X'
current_player = "X"
# current winner is always none
winner = None
# game status
game_running = True

# printing the game board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]} | ")
    print("-----------")
    print(f"{board[3]} | {board[4]} | {board[5]} | ")
    print("-----------")
    print(f"{board[6]} | {board[7]} | {board[8]} | ")
    print("-----------")


# asking player input
def player_input(board):
    try:
        inp = int(input("Enter a number 1-9: "))

        if inp >=1 and inp<=9 and board[inp-1] == "-":
            board[inp-1] = current_player
            print("\n")

        else:
            print("position already occupied")
            print("\n")
        
    except ValueError:
        print("input MUST be a number !")
        print("\n")

    # if inp >=1 and inp<=9 and board[inp-1] == "-":
    #     board[inp-1] = current_playera
    #     print("\n")
    # else:
    #     print("position already occupied")
    #     print("\n")

# check for win or tie
def checkHorizontal(board):
    global winner

    if board [0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    

def checkRow(board):
    global winner

    if board [0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    
    elif board [1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    
    elif board [2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkDiagonal(board):
    global winner

    if board [0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    
    elif board [2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def checkTie(board):
    global game_running
    if "-" not in board:
        winner = "Tie"
        print_board(board)
        print(winner)
        game_running = False

def checkWin():
    global game_running, winner1
    if checkDiagonal(board) or checkHorizontal(board) or checkRow(board):
        print(f"The winner is {winner}")
        print_board(board)
        game_running = False
        

# switch player

def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"

    else:
        current_player = "X"


while game_running:
    print_board(board)
    player_input(board)
    checkWin()
    checkTie(board)
    switch_player()
