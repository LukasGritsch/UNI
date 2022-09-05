def isPrim(n):
    if n < 2:
        return False
    else:
        for i in range(2,n):
            if n % i == 0:
                return False

    return True 
    

for i in range(1,100):
    if isPrim(i):
        print(i) 
#print(isPrim(4))