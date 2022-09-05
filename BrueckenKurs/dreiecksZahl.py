
def getNextDreieckZahl(n):
    return n*(n+1)//2

def getNextPentagonZahl(n):
    return n * (3*n -1)//2

def getNextHexanolZahl(n):
    return n*(2*n-1)

def isPentagonalZahl(aDreiecksZahl):
    for i in range(166,99999):
        hPentZahl = getNextPentagonZahl(i)
        if(hPentZahl == aDreiecksZahl ):
            return True
        elif(getNextPentagonZahl(i) > aDreiecksZahl):
            return False


def isHexanolZahl(aDreiecksZahl):
    for i in range(144,99999):
        if(getNextHexanolZahl(i) == aDreiecksZahl ):
            return True
        elif(getNextHexanolZahl(i) > aDreiecksZahl):
            return False

for i in range(286,99999):
    hNextZahl = getNextDreieckZahl(i)
    isHex = isHexanolZahl(hNextZahl)
    isPent = isPentagonalZahl(hNextZahl)
    #print(isHex)
    #print(isPent)
    if isHex and isPent :
        print(hNextZahl)
        #1533776805
        break

