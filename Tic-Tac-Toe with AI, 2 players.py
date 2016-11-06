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
    
    return board2, pos1, button, a, aiturn


def aiplay(board2, pos1, a, button, aiturn):
    """ chose a random number and play it"""
    pos1 = "".join(random.sample(["0", "1", "2", "3", "4", "5", "6", "7", "8"], 1))
 
    for i in range(len(board2)):
        for n in range(len(board2[i])):
            if str(board2[i][n]) == str(pos1):
                print(str(board2[i][n]), " is the changed value")
                board2[i][n] = "O"
                options[str(pos1)]()
                aiturn = True
 
                return board2, pos1, a, button, aiturn
    else:
        # repeat if choice is taken
        board2, pos1, a, button, aiturn = aiplay(board2, pos1, a, button, aiturn)
        return board2, pos1, a, button, aiturn
 
 
def win():
    """check win state"""
    for i in range(3):
 
        if "XXX" == str("".join(board2[i][0:3])) or "XXX" == (board2[0][i] + board2[1][i] + board2[2][i]):
            reset(1)
            aiturn = True
            if player:
                a[0] = "X"
            return aiturn
 
    if (board2[0][0] + board2[1][1] + board2[2][2]) == "XXX" or (
                    board2[0][2] + board2[1][1] + board2[2][0]) == "XXX":
        reset(1)
        aiturn = True
        if player:
            a[0] = "X"
        return aiturn
 
    for i in range(3):
 
        if "OOO" == str("".join(board2[i][0:3])) or "OOO" == (board2[0][i] + board2[1][i] + board2[2][i]):
            reset(2)
 
    if (board2[0][0] + board2[1][1] + board2[2][2]) == "OOO" or (
                    board2[0][2] + board2[1][1] + board2[2][0]) == "OOO":
        reset(2)
 
    info = 0
    for i in range(3):
        for n in range(3):
            if board2[i][n] == "X":
                info += 1
 
            if board2[i][n] == "O":
                info += 1
 
    if info == 9:
        reset(0)
        aiturn = True
        return aiturn

def reset(n):
    """ win state, reset board """
    if n == 0:
        tkinter.messagebox.showinfo('No one won', 'No one won, restarting')
    else:
        tkinter.messagebox.showinfo('There is a winner!', 'Player ' + str(n) + ' is the winner!')
    numb = 0
    button1["text"] = " "
    button2["text"] = " "
    button3["text"] = " "
    button4["text"] = " "
    button5["text"] = " "
    button6["text"] = " "
    button7["text"] = " "
    button8["text"] = " "
    button9["text"] = " "
    for i in range(len(board2)):
        for n in range(len(board2[i])):
            board2[i][n] = str(numb)
            numb += 1
 
    return board2

""" *** Layout *** """
 
button1 = ttk.Button(root, text=" ", command=lambda: turn("0", board2, button1, a))
button2 = ttk.Button(root, text=" ", command=lambda: turn("1", board2, button2, a))
button3 = ttk.Button(root, text=" ", command=lambda: turn("2", board2, button3, a))
button4 = ttk.Button(root, text=" ", command=lambda: turn("3", board2, button4, a))
button5 = ttk.Button(root, text=" ", command=lambda: turn("4", board2, button5, a))
button6 = ttk.Button(root, text=" ", command=lambda: turn("5", board2, button6, a))
button7 = ttk.Button(root, text=" ", command=lambda: turn("6", board2, button7, a))
button8 = ttk.Button(root, text=" ", command=lambda: turn("7", board2, button8, a))
button9 = ttk.Button(root, text=" ", command=lambda: turn("8", board2, button9, a))
 
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
 
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
 
button1.grid(row=0, column=0, sticky="nsew", padx=4, pady=4)
button2.grid(row=0, column=1, sticky="nsew", padx=4, pady=4)
button3.grid(row=0, column=2, sticky="nsew", padx=4, pady=4)
button4.grid(row=1, column=0, sticky="nsew", padx=4, pady=4)
button5.grid(row=1, column=1, sticky="nsew", padx=4, pady=4)
button6.grid(row=1, column=2, sticky="nsew", padx=4, pady=4)
button7.grid(row=2, column=0, sticky="nsew", padx=4, pady=4)
button8.grid(row=2, column=1, sticky="nsew", padx=4, pady=4)
button9.grid(row=2, column=2, sticky="nsew", padx=4, pady=4)
 
root.mainloop()