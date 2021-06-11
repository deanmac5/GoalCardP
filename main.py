from tkinter import *


# testing data
goal_list = {"Fly to the moon", "Coach Magpies", "Run Marathon", "Cook Crocenbush"}


window = Tk()
window.title("Goal Card")
window.config(padx=50, pady=20)

myFrame = Frame(window).place(x=50,y=100)
for g in goal_list:
    Label(myFrame, text = "- " + g).pack()


window.mainloop()
