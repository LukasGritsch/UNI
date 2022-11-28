#Beispiel Klausur

def isPrim(n):
    if n < 2:
        return False
    else:
        for i in range(1,n+1//2):
            if n != i and n % i == 0 and i != 1:
                return False
    return True
    

print(isPrim(1000))

def isProth(m):
    for n in range(1,m+1):
        if 2**n <= m:
            for k in range(1,2**n,2):
                if k*2**n +1 == m:
                    return True
        else:
            return False

print(isProth(1000))


def findProthPrim(n,m):
    hSum = 0
    for i in range(n,m+1):
        if isPrim(i) and isProth(i):
            print(i)
            hSum = hSum +i
    return hSum

print("Ergebnis: "+str(findProthPrim(1, 1000)))
        