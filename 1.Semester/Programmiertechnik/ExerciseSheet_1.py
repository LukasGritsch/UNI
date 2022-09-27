from pyparsing import *
import re

def bnf():
    protocol = Literal("http") ^ Literal('https')
    serverPart = Word('abcdefghijklmnopqrrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    server = serverPart + OneOrMore('.'+serverPart)
    pathPart = Word('abcdefghijklmnopqrrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-')
    path = OneOrMore('/' + pathPart)
    port = ':' + Word(nums)
    url =  protocol + '://' + server + Optional(port) + Optional(path) 

    url.run_tests("https://mars.mci4me.at:8000/test/test2/test3")
    url.run_tests("http://www.google.com")
    url.run_tests("https://www.mci.edu/en/universtity/the-mci/team-faculty")



def mail():
    
    #Valid adress = "gl1575@mci4me.at"
    #Invalid Adress1 = "gl1575@-mci4me.at"
    #Invalid Adress2 = "gl1575@mci4me.a5t"

    hadresses = ["gl1575@mci4me.at","gl1575@-mci4me.at","gl1575@mci4me.a5t"]

    for adress in hadresses:
        x = re.search(r"^[^.]([a-z]|[A-Z]|\d|\&|\+|\-|\=|\_|\~|\.)+\@[a-z]([a-z]|[A-Z]|\d|\-)+(\.[a-z]{2,3})?\.[a-z]{2,3}", adress)
        if x is not None:
            print(x.string+ ' is a Valid Mailadress') 
        else:
            print(adress + ' is not a Valid Mailadress')

bnf()
print()
mail()
    