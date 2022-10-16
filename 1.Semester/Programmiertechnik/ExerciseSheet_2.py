import re

def testHtmlString():
    #Beispiel von W3-Schools: https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_image_test
    target_strings = ["<img src=\"img_girl.jpg\" alt=\"Girl in a jacket\">", "<img alt=\"Girl in a jacket\" src=\"img_girl.jpg\">"]
    for target_string in target_strings:
        result = re.search(r"(\<img src=\"(\b[a-z,A-Z,\_, ]+\.(\bjpg|gif|bmp))\" alt=\"(\b[a-z,A-Z, ]+)\"\>)|(\<img alt=\"(\b[a-z,A-Z, ]+)\" src=\"(\b[a-z,A-Z,\_, ]+\.(\bjpg|gif|bmp))\"\>)", target_string)
        if result == None:
            print("Keine Images gefunden")
            return
        print(result.groups())
        for group in result.groups():
            if group != None:
                print(group) 


def getVarA():
    print("Bitte geben Sie ein ganze Zahl ein.")
    hEin = input()
    try:
        a = int(hEin)
        return a
    except:
        print("Eingabe muss ein ganze Zahl sein!")
        return getVarA() 

def getVarB():
    b = getVarA()
    if b != 0:
        return b
    else:
        print("Eingabe muss ein ganze Zahl sein und darf nicht 0 sein!")
        return getVarB()

def divMitrest():
    a = getVarA()
    b = getVarB()

    c = a/b
    
    print(c)

print("Wollen Sie dividieren oder einen image String testen? [d/i]")
hIn = input()
if hIn == 'd': 
    divMitrest()
elif hIn == 'i':  
    testHtmlString()