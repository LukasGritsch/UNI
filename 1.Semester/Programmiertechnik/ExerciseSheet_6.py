def is_odd(x):
    return _odd(x) == 0
    
    
def _odd(x):
    if x > 0 :
        return _notOdd(x-1)  
    else:
        return 0

def _notOdd(x):
    if x > 0:
        return _odd(x-1)
    else:
        return 1
    
#print(is_odd(16))

def ggt(x,y):
   return _ggtReq(x, y, x, y) 
   
        
def _ggtReq(x,y,orgx,orgy):
    if x > y:
        if x % y == 0 and orgy % y == 0:
            return y
        else:
            return _ggtReq(x, y-1,orgx,orgy)
    else:
        if y % x == 0 and orgx % x == 0:
            return x
        else:
            return _ggtReq(y, x-1,orgx,orgy)

#print(ggt(33, 23))


def nested_sum(aArray):
    hSum = 0
    for i in aArray:
        if isinstance(i, list):
            hSum = hSum + nested_sum(i)
        elif isinstance(i, int):
             hSum = hSum + i
    return hSum
        

print(nested_sum([5, [4, "3"], 4, [3, [2.5, [1, 1]]]]))




def sigma(n):
    hSum = 0
    for i in range(1,n+1):
       if n % i == 0:
           hSum = hSum + i
    return hSum

def S(m,d):
    i = 1
    hSum = 0
    while i <= m:
        if sigma(i) % d == 0:
            hSum = hSum + i
        i = i + 1
    return hSum
           
#print(S(20, 7))

def isPrim(n):
    if n == 2:
        return True
    
    for i in range(2,n+1):
        if n % i == 0 and n != i:
            return False
    
    return True

def twinPrimeSum(x):
    hRetList = []
    i = 2
    hFoundPrim = 0
    hWaitingPosition = 0
    while hFoundPrim <= x:
        if isPrim(i):
            hFoundPrim = hFoundPrim +1
            
            if i < 3:
                i = i + 1
                continue
            
            if len(hRetList) == 0:
                hRetList.append(i)
            else:
                hTemp = hRetList[len(hRetList)-1]
                if i - hTemp == 2:
                    hRetList.append(i)
                    hWaitingPosition = 0
                
                if i - hWaitingPosition == 2:
                    hRetList.append(hWaitingPosition)
                    hRetList.append(i)
                    hWaitingPosition = 0
                    
                else:
                    hWaitingPosition = i
        i = i + 1
    
    hSum = 0
    for k in hRetList:
        hSum = hSum + k
        
    return hSum

print(twinPrimeSum(6))



        