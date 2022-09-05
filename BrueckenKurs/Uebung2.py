from operator import mod


def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

def isEvenWithoutIf(n):
    return n % 2 == 0

print(isEven(4))
print(isEvenWithoutIf(4))