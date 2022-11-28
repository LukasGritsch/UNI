def isPrim(n):
    if n < 2:
        return False
    else:
        for i in range(1,n+1//2):
            if n != i and n % i == 0 and i != 1:
                return False
    return True

def rotateNumber(n):
    hStr = str(n)
    hRet = []
    
    while len(hRet) < len(hStr)-1:
        hTmp = hStr[0]
        temp = list(hStr)
        for i in range(len(hStr)):
            if i > 0:
                temp[i-1] =  temp[i]
        temp[len(hStr)-1] = hTmp
        hStr = "".join(temp)
        hRet.append(int(hStr))
      
    return hRet


def iszirkPrim(n):
    if isPrim(n):
        hRotNumbers = rotateNumber(n)
        for i in hRotNumbers:
            if not isPrim(i):
                return False
        return True
    return False
        
print(iszirkPrim(999331))
        
def getzirkPrimBetween0And(n):
    hCnt = 0
    for i in range(n+1):
        if isPrim(i):
            if iszirkPrim(i):
                hCnt = hCnt +1
                print(i)
    return hCnt

print(getzirkPrimBetween0And(1000000))
        
            
    