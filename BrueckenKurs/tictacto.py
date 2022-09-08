import os

fGameField = [['-','-','-'],['-','-','-'],['-','-','-']]
fIsPlayerOneTurn = True
fPlayerOneSign = ""
fPlayerTwoSign = ""

def newGame():
    global fGameField
    for i in range(3):
        for j in range(3):
            fGameField[i][j] = '-'
    global fPlayerOneSign 
    fPlayerOneSign = input("PlayerOne type in your sign: ")
    global fPlayerTwoSign 
    fPlayerTwoSign = input("PlayerTwo type in your sign: ")

def printBoard():
    hBoardStr = ""
    for i in range(3):
        for j in range(3):
            global fGameField
            #print(str(i)+","+str(j))
            hBoardStr = hBoardStr + " " + fGameField[i][j]
            if j == 2:
                hBoardStr = hBoardStr +"\n"
    print(hBoardStr)

def isPositionFree(aPosition):
    global fGameField
    if fGameField[int(aPosition[0])][int(aPosition[1])] == '-':
        return True
    else:
        return False

def getPosition(aPosition):
    if isinstance(aPosition,str):
        if "," in aPosition:
            hPositions = aPosition.split(",") 
            if isPositionFree(hPositions):
                return hPositions
            else:
                print("Place already taken")
                return None
        else:
            print("Wrong Input")
            return None

def isLineWon():
    global fGameField
    global fPlayerOneSign
    global fPlayerTwoSign
    for i in range(3):
        hLine = fGameField[i]
        oneWon = hLine[0] == fPlayerOneSign and hLine[1] == fPlayerOneSign and hLine[2] == fPlayerOneSign
        twoWon = hLine[0] == fPlayerTwoSign and hLine[1] == fPlayerTwoSign and hLine[2] == fPlayerTwoSign
        if oneWon:
            return 1
        elif twoWon:
            return 2
    return 0

def isColWon():
    global fGameField
    global fPlayerOneSign
    global fPlayerTwoSign
    for i in range(3):
  
        oneWon = fGameField[0][i] == fPlayerOneSign and fGameField[1][i] == fPlayerOneSign and fGameField[2][i] == fPlayerOneSign
        twoWon = fGameField[0][i] == fPlayerTwoSign and fGameField[1][i] == fPlayerTwoSign and fGameField[2][i] == fPlayerTwoSign

        if oneWon:
            return 1
        elif twoWon:
            return 2
    return 0

def isDiagWon():
    global fGameField
    global fPlayerOneSign
    global fPlayerTwoSign
    oneWonPos = fGameField[0][0] == fPlayerOneSign and fGameField[1][1] == fPlayerOneSign and fGameField[2][2] == fPlayerOneSign
    twoWonPos = fGameField[0][0] == fPlayerTwoSign and fGameField[1][1] == fPlayerTwoSign and fGameField[2][2] == fPlayerTwoSign
    oneWonDeg = fGameField[0][2] == fPlayerOneSign and fGameField[1][1] == fPlayerOneSign and fGameField[2][0] == fPlayerOneSign
    twoWonDeg = fGameField[0][2] == fPlayerTwoSign and fGameField[1][1] == fPlayerTwoSign and fGameField[2][0] == fPlayerTwoSign
    if oneWonPos or oneWonDeg:
        return 1
    elif twoWonPos or twoWonDeg:
        return 2
    return 0

def isFull():
    global fGameField
    for i in range(3):
        for j in range(3):
            if fGameField[i][j] == '-':
                return False
    return True

def isGameOver():
    if isLineWon() == 1 or isColWon() == 1 or isDiagWon() == 1:
        print("PlayerOne Won!")
        return True 
    elif isLineWon() == 2 or isColWon() == 2 or isDiagWon() == 2:
        print("PlayerTwo Won!")
        return True
    elif isFull():
        print("Even!")
        return True
    return False


newGame()

while not isGameOver():
    printBoard()
    if fIsPlayerOneTurn:
        hPositionStr = input("PlayerOne please provide your position\n")
        hPosition = getPosition(hPositionStr)
        if hPosition is not None:
            fGameField[int(hPosition[0])][int(hPosition[1])] = fPlayerOneSign
            fIsPlayerOneTurn = False
            os.system('clear')
        else:
            print("Wrong Input")
    else:
        hPositionStr = input("PlayerTwo please provide your position\n")
        hPosition = getPosition(hPositionStr)
        if hPosition is not None:
            fGameField[int(hPosition[0])][int(hPosition[1])] = fPlayerTwoSign
            fIsPlayerOneTurn = True
            os.system('clear')
        else:
            print("Wrong Input")