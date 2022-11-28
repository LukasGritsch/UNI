#Funktion zu Testen ob eine Zahl eine Primzahl ist
def isPrim(n):
    if n < 2:
        return False
    else:
        for i in range(1,n+1//2):
            if n != i and n % i == 0 and i != 1:
                return False
    return True

#hPrimToTest = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,]
#for i in hPrimToTest:
#    print(isPrim(i))

#Funktion, welche eine Zahl rueckwerts gelesen retour gibt
def getReverseValue(n):
    return int(str(n)[::-1])

#print(getReverseValue(679))

#Funktion, welche überprüft, ob die übergebene Zahl ein Palindrom ist
def isPalindrom(n):
    return n == getReverseValue(n)
    
#print(isPalindrom(131))

#Funktion, welche überprüft ob die übergeben Zahl eine Mirpzahl ist
def isMir(n):
    if isPrim(n) and not isPalindrom(n) and isPrim(getReverseValue(n)):
        return True
    return False

#Testdaten aus dem Internet
#for i in [13,17,31,37,71,73,79,97,107,113,149,157,167,179,
# 199,311,337,347,359,389,701,709,733,739,743,751,
# 761,769,907,937,941,953,967,971,983,991,1009,1021,
# 1031,1033,1061,1069,1091,1097,1103,1109,1151,1153,
# 1181,1193,1201]:
#    print(isMir(i))

#Funktion welche die Ziffern in einer Zahl zählt
def countZiffer(n,ziffer):
    hTempStr = str(n)
    hCnt = 0
    for i in range(len(hTempStr)):
        if int(hTempStr[i]) == ziffer:
            hCnt = hCnt +1
    return hCnt

#Funktion laut Klausurangabe
def M(n,m):
    hSum = 0
    for i in range(n,m+1):
        if isMir(i) and countZiffer(i, 1) == 2:
               hSum = hSum + i
    return hSum

#Aufruf der Funktion
print(M(100, 1100))
