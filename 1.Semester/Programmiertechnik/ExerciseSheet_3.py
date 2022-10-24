#Aufgabe 1
def is_odd(x):
    result = None
    
    result = (x % 2 == 0)
    
    return not result

print(is_odd(13))

#Aufgabe 2
def my_sum(x):
    sum = 0
    
    hNumberToAdd = 3
    
    while hNumberToAdd < x:
        sum = sum + hNumberToAdd
        hNumberToAdd = hNumberToAdd + 5   
    
    return sum

print(my_sum(132))

#Aufgabe 3
def get_min_max(a, b, c, d, e, f):
    _max_ = None
    _min_ = None
    hArray = [a,b,c,d,e,f]
    for variable in hArray:
        if(_max_ == None):
            _max_ = variable
        if(_min_ == None):
            _min_ = variable
        if(variable < _min_):
            _min_ = variable
        if(variable > _max_):
            _max_ = variable
    return _min_, _max_

print(get_min_max(21, 23, 13, 44, 5, 26))

#Aufgabe 4
def count_loop(x):
    count = 0
    while not is_odd(x):
        count = count +1
        x = x / 2
    
    return count

print(count_loop(48))

#Aufgabe5
def division_mit_rest(x, y):
    result = 0
    remainder = 0
    
    hPlaceHolder = y
    
    while hPlaceHolder <= x:
        result = result +1
        hPlaceHolder = hPlaceHolder +y
    
    if result == 0 and x > y :
        result = 1

    remainder = x - (result * y)
    
    return result, remainder

print(division_mit_rest(4, 2))

#Aufgabe6
def is_prime(x):
    if x < 1:
        return False

    for i in range(1,x):
        if i == 1 or i == x:
            if not x % i == 0:
                return False
        elif x % i == 0:
            return False
    
    return True

print(is_prime(5))

#Aufgabe7
def is_triangular(x):
    hSum = 0
    i = 0
    while hSum < x:
        hSum = hSum +i
        i = i + 1
    return hSum == x
    

print(is_triangular(0))