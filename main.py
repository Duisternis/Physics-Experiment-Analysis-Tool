from tkinter import *
from tkinter import ttk, filedialog
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import os

from exp1 import main as main1
from exp2 import main as main2
from exp3 import main as main3

def solve(): 
    index = choice.current()
    path = nav_display.get("1.0", "end-1c")
    if index==0:
        main1(path, content, graphics, g_nav)
    elif index==1:
        main2(path, content, graphics, g_nav)
    elif index==2:
        main3(path, content, graphics, g_nav)

def open_file():
    file=filedialog.askopenfile()
    if file:
        filepath = os.path.abspath(file.name)
    nav_display.delete("1.0", "end")
    nav_display.insert(END, filepath)

root = Tk()
root.title("Graphicit")
root.geometry("1000x600")

icon = PhotoImage(file="/Users/varnan/Desktop/Project - PHYLAB/pythonProject/icon.png")
root.iconphoto(False, icon)

left = Frame(root)
right = Frame(root)
left.pack(side=LEFT)
right.pack(side=RIGHT)

nav = Frame(left, height=70, width=500)
content = LabelFrame(left, text="Content", height=500, width=480)
nav.grid(row=0, padx=5, pady=5)
content.grid(row=1, padx=5, pady=5)

graphics = LabelFrame(right, text="Graphs & Tables", height=510, width=480)
g_nav = LabelFrame(right, text="Navigation Pane", height=50, width=480)
graphics.grid(row=0, padx=5, pady=5)
g_nav.grid(row=1, padx=5, pady=5)


choice = ttk.Combobox(
    nav,
    state="readonly",
    values=[
        "1. Ohm's Law",
        "2. Numeric Aperture",
        "3. Bending Loss"
    ],
    width=15
)
choice.grid(row=0, column=0, pady=6, padx=6)

nav_display = Text(nav, height=3, width=30)
nav_display.grid(row=0, column=2, padx=10, rowspan=2)

browse = Button(nav, text="BROWSE", command=open_file)
browse.grid(row=0, column=1)

submit = Button(nav, text="SUBMIT", command=solve, width=20)
submit.grid(row=1, column=0, columnspan=2, pady=3)


root.mainloop()