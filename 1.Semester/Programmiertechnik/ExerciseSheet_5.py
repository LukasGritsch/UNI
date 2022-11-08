
from turtle import hideturtle


def search_array(array, x):    
    hIdx = 0
    for i in array:
        if i == x:
            return hIdx
        hIdx = hIdx + 1
    return None

print(search_array([1,2,3,3, 4,5 ,3 ], 3))



def selection_sort(array, asc):  
    hIdxSortet = 0
    while hIdxSortet < len(array):
        hIdxSmalest = hIdxSortet
        for i in range(hIdxSortet,len(array)):
            if asc:
                if array[i] < array[hIdxSmalest]:
                    hIdxSmalest = i
            else:
                if array[i] > array[hIdxSmalest]:
                    hIdxSmalest = i
        hTmp = array[hIdxSortet]
        array[hIdxSortet] = array[hIdxSmalest]
        array[hIdxSmalest] = hTmp
        hIdxSortet = hIdxSortet + 1
    return array

print(selection_sort([2,4,6,5,3,1], False))

def sum_array(array):
    hSum = 0
    hIdx = 0

    while hIdx < len(array):
        if isinstance(array[hIdx],int):
            hSum = hSum + array[hIdx]
        hIdx = hIdx + 1
    
    return hSum

print(sum_array(["Hello", 2, "World", True, 3, 4.5]))

def push(stack, element):
    stack.append(element)

stack = []

def pop(stack):
    hRet = None
    if len(stack) == 0:
        return None
    else:
        hRet = stack[len(stack)-1]
        del stack[len(stack)-1]
    return hRet

def top(stack):
    return stack[len(stack) -1]

def is_empty(stack):
    return len(stack) == 0

def size(stack):
    return len(stack)

#Create an empty stack
stack = []

#Print the stack - expected output: []
print("Stack: " + str(stack))

#Pushing an element onto the stack
print("Pushing element: \"Hello\"");
push(stack, "Hello")

#Print the stack - expected output: ['Hello']
print("Stack: " + str(stack))

#Check if the stack is empty
print("Empty?: " + str(is_empty(stack)))

#Pushing an element onto the stack
print("Pushing element: 5");
push(stack, 5)

#Print the stack - expected output: ['Hello', 5]
print("Stack: " + str(stack))

#Check the size of the stack
print("Size: " + str(size(stack)))

#Retrieve the top element of the stack
print("Top: " + str(top(stack)))

#Print the stack - expected output: ['Hello', 5]
print("Stack: " + str(stack))

#Retrieve the top element of the stack and delete it
print("Pop: " + str(pop(stack)))

#Print the stack - expected output: ['Hello']
print("Stack: " + str(stack))

#Check the size of the stack
print("Size: " + str(size(stack)))

#Retrieve the top element of the stack and delete it
print("Pop: " + str(pop(stack)))

#Check if the stack is empty
print("Empty?: " + str(is_empty(stack)))

#Print the stack - expected output: []
print("Stack: " + str(stack))


def get_digits(n):
    hDigitAsString = str(n)
    hRetList = []
    for i in range(0,len(hDigitAsString)):
        hRetList.append(int(hDigitAsString[i]))
    return hRetList

print(get_digits(13442))


def digit_power_sum(digits, power):
   return sum_array(digits)**power

print(digit_power_sum([2, 3, 1], 3))

def is_interesting_number(n):
    if n < 2:
        return False

    hIdx = 1
    hNumber = 0
    while  hNumber < n:
        hNumber = digit_power_sum(get_digits(n),hIdx)
        if hNumber == n:
            return True
        elif hNumber == 1:
            return False 
        hIdx = hIdx +1

    return False

print(is_interesting_number(512))

def get_interesting_numbers(l,u):
    hRetList = []
    for i in range(l,u):
        if i == 4913:
            print(i)
        if is_interesting_number(i):
            hRetList.append(i)
    return hRetList

print(get_interesting_numbers(10, 10000))

def digits_factorial(n):
    hRet = 0
    for i in range(3,n):
        hDigits = get_digits(i)
        hSum = 0
        for d in hDigits:
            hTeilSum = 1
            for fakul in range(1,d+1):
                hTeilSum = hTeilSum * fakul
            hSum = hSum + hTeilSum
        if hSum == i:
            hRet = hRet + i
    return hRet

print(digits_factorial(1000))

exercise_5_7_result = ["a","b","c","d","g"]