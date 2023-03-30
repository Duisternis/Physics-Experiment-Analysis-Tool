from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

root = Tk()
root.geometry("1000x1000")

frame_left = Frame(root, height=400, width=400)
frame_left.pack(side=LEFT)
frame_right = Frame(root, height=400, width=400)
frame_right.pack(side=RIGHT)

x = [1, 2, 3, 4, 5, 6]
y = [10, 20, 30, 40, 50, 60]

fig = plt.figure(figsize=(5, 4), dpi=100)

axes = fig.add_axes([0.1, 0.1, 0.9, 0.9])

axes.set_xlabel("Voltage (V)")
axes.set_ylabel("Current (mA)")
axes.set_title("Resistance Graph")

axes.plot(x, y, label="R = V/I")
axes.legend(loc=0)

canvas = FigureCanvasTkAgg(fig, master=frame_left)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, frame_left)
toolbar.update()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

root.mainloop()