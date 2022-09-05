from cgitb import text
from random import randint
import tkinter

window = tkinter.Tk()

window.title("Simple_dice_game")
window.geometry("400x200")

hCurrentMony = 10
rolledStrInString = ""

hTextCurrentMony = tkinter.Label(window,text="Current Mony:").grid(row=0,column=0)
hTextCurrentMonyAmount = tkinter.Label(window,text=""+str(hCurrentMony)+"€" ).grid(row=0,column=1)

hCurentRoll = tkinter.Label(window,text="Current Roll:").grid(row=1,column=0)
hCurentRollAmount = tkinter.Label(window,text=rolledStrInString)
hCurentRollAmount.grid(row=1,column=1)

def rollDices():
     rolledNumber = randint(1,6)
     if rolledNumber != 0: 
        hCurentRollAmount.configure(text=""+str(rolledNumber))

rollTheDiceButton = tkinter.Button(window,text="Roll the dices",command=rollDices).grid(row=2,column=0)

window.mainloop()







