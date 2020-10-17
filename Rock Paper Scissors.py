# Rock Paper Scissors (Fully Operational)
from tkinter import *
import random
from time import *

def want_to_play():
    global windowOne
    windowOne = Tk()
    global buttonA
    global buttonB
    buttonA = Button(windowOne, text="Play Rock Paper Scissors", command=display)
    buttonB = Button(windowOne, text="Exit Game Menu", command=exit)
    buttonA.pack()
    buttonB.pack()    

def display():
    global ButtonA1
    global ButtonB1
    global ButtonC1
    ButtonA1 = Button(windowOne, text="Rock", command=lambda: setchoice("rock"))
    ButtonB1 = Button(windowOne, text="Paper", command=lambda: setchoice("paper"))
    ButtonC1 = Button(windowOne, text="Scissors", command=lambda: setchoice("scissors"))
    buttonA.pack_forget()
    buttonB.pack()
    ButtonA1.pack()
    ButtonB1.pack()
    ButtonC1.pack()

def setchoice(x):
    global choice
    choice = x
    rockpaperscissors()

def setchoice2(x):
    global choice
    choice = x
    rockpaperscissorsreplay()

def display2():
    global windowThree
    windowThree = Tk()
    exitButton = Button(windowThree, text="Exit Game", command=exit)
    ButtonA2 = Button(windowThree, text="Rock", command=lambda: setchoice2("rock"))
    ButtonB2 = Button(windowThree, text="Paper", command=lambda: setchoice2("paper"))
    ButtonC2 = Button(windowThree, text="Scissors", command=lambda: setchoice2("scissors"))
    ButtonA2.pack()
    ButtonB2.pack()
    ButtonC2.pack()
    exitButton.pack()

def rockpaperscissors():
    windowOne.destroy()
    x1 = ["rock", "paper", "scissors"]
    cpu_choice = random.choice(x1)
    global windowTwo
    windowTwo = Tk()
    leave = Button(windowTwo, text="Exit End Screen", command=win2exit)
    leave.pack()

    if choice == cpu_choice:
        Text1 = Text(windowTwo, width=30, height=10)
        Text1.insert(INSERT,"CPU chose " + cpu_choice + "\nTie!")
        Text1.pack()
        Text1.config(state="disabled")
        

    elif choice == "rock" and cpu_choice == "scissors":
        Text1 = Text(windowTwo, width=30, height=10)
        Text1.insert(INSERT,"CPU chose " + cpu_choice + "\nYou Win!")
        Text1.pack()
        Text1.config(state="disabled")
        

    elif choice == "scissors" and cpu_choice == "rock":
        Text1 = Text(windowTwo, width=30, height=10)
        Text1.insert(INSERT,"CPU chose " + cpu_choice + "\nCPU wins!")
        Text1.pack()
        Text1.config(state="disabled")

    elif choice == "paper" and cpu_choice == "rock":
        Text1 = Text(windowTwo, width=30, height=10)
        Text1.insert(INSERT,"CPU chose " + cpu_choice + "\nYou Win!")
        Text1.pack()
        Text1.config(state="disabled")

    elif choice == "rock" and cpu_choice == "paper":
        Text1 = Text(windowTwo, width=30, height=10)
        Text1.insert(INSERT,"CPU chose " + cpu_choice + "\nCPU wins!")
        Text1.pack()
        Text1.config(state="disabled")

    elif choice == "scissors" and cpu_choice == "paper":
        Text1 = Text(windowTwo, width=30, height=10)
        Text1.insert(INSERT,"CPU chose " + cpu_choice + "\nYou Win!")
        Text1.pack()
        Text1.config(state="disabled")

    elif choice == "paper" and cpu_choice == "scissors":
        Text1 = Text(windowTwo, width=30, height=10)
        Text1.insert(INSERT,"CPU chose " + cpu_choice + "\nCPU wins!")
        Text1.pack()
        Text1.config(state="disabled")

    else:
        Text1 = Text(windowTwo, width=30, height=10)
        Text1.insert(INSERT,"Hey! You didn't pick rock, paper or scissors!")
        Text1.pack()
        Text1.config(state="disabled")
        
    display2()

def rockpaperscissorsreplay():
    x1 = ["rock", "paper", "scissors"]
    cpu_choice = random.choice(x1)
    windowThree.destroy()
    global windowTwo
    windowTwo = Tk()
    leave = Button(windowTwo, text="Exit End Screen", command=win2exit)
    leave.pack()

    if choice == cpu_choice:
        Text1 = Text(windowTwo, width=30, height=10)
        Text1.insert(INSERT,"CPU chose " + cpu_choice + "\nTie!")
        Text1.pack()
        Text1.config(state="disabled")

    elif choice == "rock" and cpu_choice == "scissors":
        Text1 = Text(windowTwo, width=30, height=10)
        Text1.insert(INSERT,"CPU chose " + cpu_choice + "\nYou Win!")
        Text1.pack()
        Text1.config(state="disabled")
        
    elif choice == "scissors" and cpu_choice == "rock":
        Text1 = Text(windowTwo, width=30, height=10)
        Text1.insert(INSERT,"CPU chose " + cpu_choice + "\nCPU wins!")
        Text1.pack()
        Text1.config(state="disabled")
        
    elif choice == "paper" and cpu_choice == "rock":
        Text1 = Text(windowTwo, width=30, height=10)
        Text1.insert(INSERT,"CPU chose " + cpu_choice + "\nYou Win!")
        Text1.pack()
        Text1.config(state="disabled")
        
    elif choice == "rock" and cpu_choice == "paper":
        Text1 = Text(windowTwo, width=30, height=10)
        Text1.insert(INSERT,"CPU chose " + cpu_choice + "\nCPU wins!")
        Text1.pack()
        Text1.config(state="disabled")
        
    elif choice == "scissors" and cpu_choice == "paper":
        Text1 = Text(windowTwo, width=30, height=10)
        Text1.insert(INSERT,"CPU chose " + cpu_choice + "\nYou Win!")
        Text1.pack()
        Text1.config(state="disabled")
        
    elif choice == "paper" and cpu_choice == "scissors":
        Text1 = Text(windowTwo, width=30, height=10)
        Text1.insert(INSERT,"CPU chose " + cpu_choice + "\nCPU wins!")
        Text1.pack()
        Text1.config(state="disabled")
        
    else:
        Text1 = Text(windowTwo, width=30, height=10)
        Text1.insert(INSERT,"Hey! You didn't pick rock, paper or scissors!")
        Text1.pack()
        Text1.config(state="disabled")

    display2()

def win2exit():
    windowTwo.destroy()
        
want_to_play()
