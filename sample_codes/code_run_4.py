from tkinter import *
import pandas as pd
import matplotlib.pylab as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

def clear_frame():
   for widgets in frame_right.winfo_children():
      widgets.destroy()

def display_1():

    clear_frame()

    x = [1, 2, 3, 4, 5]
    y = [10, 20, 30, 40, 50]

    fig = plt.figure(figsize=(5, 4), dpi=100)
    fig.add_subplot(111).plot(x, y, color="green", linestyle="--", label="Value Ω")     # add one more to add more lines

    plt.title("Resistance Graph (Voltage vs Ampere)")
    plt.xlabel("Voltage (V)")
    plt.ylabel("Current (mA)")
    plt.legend(loc="best")

    canvas = FigureCanvasTkAgg(fig, frame_right)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, frame_right)
    toolbar.update()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

def display_2():

    clear_frame()

    x = [1, 3, 6, 8, 12]
    y = [10, 49, 30, 50, 70]

    fig = plt.figure(figsize=(5, 4), dpi=100)
    fig.add_subplot(111).plot(x, y)


    canvas = FigureCanvasTkAgg(fig, frame_right)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, frame_right)
    toolbar.update()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

def display_3():

    clear_frame()

    Yscroll = Scrollbar(frame_right)
    Yscroll.pack(side=RIGHT, fill=Y)
    Xscroll = Scrollbar(frame_right, orient="horizontal")
    Xscroll.pack(side=BOTTOM, fill=X)

    textarea = Text(frame_right, wrap=NONE, yscrollcommand=Yscroll.set, xscrollcommand=Xscroll.set, height=25, width=54)
    Yscroll.config(command=textarea.yview)
    Xscroll.config(command=textarea.xview)
    textarea.pack(expand=1, fill=BOTH, padx=50, pady=50)

    header_names = pd.DataFrame([
    ["Readings", "Voltage (V)"],
    ["Readings", "Current (mA)"],
    ["Resistance (Ω)", ""]],
    columns = ["S.No", ""])

    rows = [
        [1.0, 10.0, 0.1], 
        [2.0, 20.0, 0.1], 
        [3.0, 30.0, 0.1], 
        [4.0, 40.0, 0.1], 
        [5.0, 50.0, 0.1]
    ] 

    header = pd.MultiIndex.from_frame(header_names)
    index = [i for i in range(1, len(rows)+1)]
    df = pd.DataFrame(rows, columns=header, index=index)

    textarea.insert(END, "TABLE ::\n\n\n" + df.to_string())



root = Tk()

frame_left = Frame(root, height=400, width=500, bg="red")
frame_left.pack(side=LEFT)

frame_right = Frame(root, height=400, width=500, bg="yellow")
frame_right.pack(side=RIGHT)

button1 = Button(frame_left, text="click 1", command=display_1)
button2 = Button(frame_left, text="click 2", command=display_2)
button3 = Button(frame_left, text="click 3", command=display_3)
button1.grid(row=0)
button2.grid(row=1)
button3.grid(row=2)

display_3()

root.mainloop()