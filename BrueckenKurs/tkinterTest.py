from cgitb import text
from distutils.cmd import Command
from random import randint
import tkinter
from tokenize import String
import time

window = tkinter.Tk()

window.title("Simple_dice_game")
window.geometry("400x200")

hTries = 0
hCurrentMony = 10

hTextCurrentMony = tkinter.Label(window,text="Current Mony:").grid(row=0,column=0)
hTextCurrentMonyAmount = tkinter.Label(window,text=""+str(hCurrentMony)+"€" )
hTextCurrentMonyAmount.grid(row=0,column=1)

hCurentRoll = tkinter.Label(window,text="Current Roll:").grid(row=1,column=0)
hCurentRollAmount = tkinter.Label(window,text="")
hCurentRollAmount.grid(row=1,column=1)

guessLabel = tkinter.Label(window,text="Your guess:").grid(row=2,column=0)
guess = tkinter.Entry(window)
guess.grid(row=2,column=1)

rollTheDiceButton = tkinter.Button(window,text="Roll the dices")
rollTheDiceButton.grid(row=3,column=0)

closeWindow = tkinter.Button(window,text="Close",state="disable")
closeWindow.grid(row=3,column=1)

inputErrorLbl = tkinter.Label(window,fg="red",text="")
inputErrorLbl.grid(row=5,column=1)

def wrongInput():
        inputErrorLbl.configure(text="Wrong or empty input")  

def correctInput():
        inputErrorLbl.configure(text="")  

def gameOver():
        global hTries
        inputErrorLbl.configure(text="Sorry, you lost. You have taken "+str(hTries) +" tries")
        global rollTheDiceButton
        rollTheDiceButton.configure(state="disabled")
        global closeWindow
        closeWindow.configure(state="active")

def gameWon():
        global hTries
        inputErrorLbl.configure(text="Congratulations, you won! You have taken "+str(hTries) +" tries",fg="green")
        global rollTheDiceButton
        rollTheDiceButton.configure(state="disabled")
        global closeWindow
        closeWindow.configure(state="active")

def doGuess(aInput,aDiceNumber):
        global hCurrentMony 
        if(aInput == aDiceNumber):
                hCurrentMony += 1
        else:
                hCurrentMony -= 1
        hTextCurrentMonyAmount.configure(text=""+str(hCurrentMony)+"€")

def rollDices():

     try:
        hIntput = int(guess.get())
     except:
        hIntput = 0
     if(hIntput < 1 or hIntput > 6):
        wrongInput()
     else:
        correctInput()
        rolledNumber = randint(1,6)
        hCurentRollAmount.configure(text=""+str(rolledNumber))
        doGuess(hIntput,rolledNumber)
        global hTries
        hTries += 1

     global hCurrentMony
     if hCurrentMony < 1:
        gameOver()
     elif hCurrentMony > 20:
        gameWon()

def close():
        global window
        window.destroy()

rollTheDiceButton.configure(command=rollDices)
closeWindow.configure(command=close)

window.mainloop()