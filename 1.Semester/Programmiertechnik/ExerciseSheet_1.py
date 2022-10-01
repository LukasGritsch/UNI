from pyparsing import *
import re

def bnf():
    # <protocol> ::= 'http' | 'https' 
    protocol = Literal('http') ^ Literal('https')
    # serverPart ::= 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' |
    # 'w' | 'x' | 'y' | 'z' | 'A' | 'B' | 'C' | 'D' | 'E' | 'F' | 'G' | 'H' | 'I' | 'J' | 'K' | 'L' | 'M' | 'N' | 'O' | 'P' | 'Q' | 'R' | 'S' | 'T' |
    # 'U' | 'V' | 'W' | 'X' | 'Y' | 'Z' | '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | 
    serverPart = Word('abcdefghijklmnopqrrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') 
    # <server> :== serverPart + '.' serverPart | server + . + serverPart 
    server = serverPart + OneOrMore('.'+serverPart)
    # serverPart ::= 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' |
    # 'w' | 'x' | 'y' | 'z' | 'A' | 'B' | 'C' | 'D' | 'E' | 'F' | 'G' | 'H' | 'I' | 'J' | 'K' | 'L' | 'M' | 'N' | 'O' | 'P' | 'Q' | 'R' | 'S' | 'T' |
    # 'U' | 'V' | 'W' | 'X' | 'Y' | 'Z' | '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | '-'
    pathPart = Word('abcdefghijklmnopqrrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-')
    # <path> ::= '/' + pathPart | path + '/' + pathPart 
    path = OneOrMore('/' + pathPart)
    # <nums> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
    # <port> ::= ':' + nums
    port = ':' + Word(nums)
    #<ur> ::= <protocol> + '://' + <server> <port>? <path>?
    url =  protocol + '://' + server + Optional(port) + Optional(path) 

    url.run_tests("https://mars.mci4me.at:8000/test/test2/test3")
    url.run_tests("http://www.google.com")
    url.run_tests("https://www.mci.edu/en/universtity/the-mci/team-faculty")



def mail():

    hadresses = ["gl1575@mci4me.at","gl1575@-mci4me.at","gl1575@mci4me.a5t","gl1ä575@mci4me.a5t","gl15ü75@mci4me.a5t","gl1ß575@mci4me.a5t",".gl1575@mci4me.a5t"]

    for adress in hadresses:

        x = re.search(r"^[^.-][^äöüÄÖÜß]*(?<!\.)\@[^.-](\w|\-)+[^-](\.[a-z]{2})+$", adress)
        y = re.search(r"(?!(\.))[a-zA-Z0-9\&\+\-\=\_\~\.]*(?<!\.)@(?!(\-))[a-zA-Z0-9\-]+(?<!\-)\.?([a-z]{2})\.[a-z]{2}$",adress)

        print('Für regex x:')
        if x is not None:
            print(x.string+ ' is a Valid Mailadress') 
        else:
            print(adress + ' is not a Valid Mailadress')

        print('Für regex y:')
        if y is not None:
            print(y.string+ ' is a Valid Mailadress') 
        else:
            print(adress + ' is not a Valid Mailadress')

bnf()
print()
mail()