import random
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
 
root = tk.Tk()
 
""" *** Memory *** """
board2 = [["0", "1", "2"], ["3", "4", "5"], ["6", "7", "8"]]
a = ["X"]
 
""" *** Functions *** """
player = tkinter.messagebox.askyesno("First", "Playing against another player?")
print("Is there another player? ", player)
 
 
def turn(pos1, board2, button, a):
    """ enter choice to memory and change the board and interface """
    print("playing with", a)
    for i in range(len(board2)):
        for n in range(len(board2[i])):
            if board2[i][n] == str(pos1):
                board2[i][n] = str(a[0])
 
    # toggle button text
 
    if button["text"] == " ":
        button["text"] = str(a[0])
 
        # change a to new turn
        if player:
 
            if a[0] == "X":
                a[0] = "O"
                print("changed x to o")
 
            else:
                a[0] = "X"
                print("changed o to x")
 
    else:
        print("cant, already taken")
        aiturn = True
        return aiturn
 
    # check win state
    aiturn = win()