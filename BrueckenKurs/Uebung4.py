import random
import os

def roll_dice():
    return random.randint(1,6)

def get_input ():
    return random.randint(1,6)

def run ():
    guthaben = 10
    while guthaben > 0 and guthaben < 20:
        einsatz = 10
        #if(einsatz < 0 or einsatz > guthaben):
        #    print("Falscher Einsatz")
        #   continue
    
        tipp = get_input()

        #if tipp < 1 or tipp > 6:
        #    print("Falsche Eingabe")
        #    continue
    
        guthaben = guthaben - einsatz 

        if tipp == roll_dice:
            guthaben = guthaben + (einsatz * 2)

    if(guthaben >= 20):
        return True
    else:
        return False

for i in range(1,10000):
    if(run()):
        print("Gewonnen")
        break
