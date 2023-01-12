#gameboard

board = ["-","-","-",
        "-","-","-",
        "-","-","-"]
currentPlayer = "X"
winner = None
gameRunning = True

#printing the game board

def printBoard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8])
printBoard(board)

#take player input

def playerInput(board):
    inp = int(input("Entrez un chiffre entre 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Oups, Un joueur est déjà dans cette case!")


#check for win or tie
def checkHorizontale(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] !="-":
        winner = board[0] #doesn't matter ofthe value because they are all equals
        return True
    elif board[3] == board[4] == board[5] and board[3] !="-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] !="-":
        winner = board[6]
        return True

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] !="-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] !="-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] !="-":
        winner = board[2]
        return True

def checkDiagonale(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] !="-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] !="-":
        winner = board[2]
        return True

def checkTIE(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("C'est une égalité !")
        gameRunning = False
        winner = False

def checkWin():
    if checkDiagonale(board) or checkHorizontale(board) or checkRow(board):
        print(f"Le Gagnant est {winner}")

#switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer ="O"
    else:
        currentPlayer ="X"


#check for win or tie again

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTIE(board)
    switchPlayer()