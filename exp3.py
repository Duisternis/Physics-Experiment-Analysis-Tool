import csv
import math
from tkinter import *
import pandas as pd
from pandastable import Table
import matplotlib.pylab as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

def clear_frame(frame):
   for widgets in frame.winfo_children():
      widgets.destroy()

def solve(path):
    csv_content_list = []
    result = []
    with open(path, "rt") as file:
        data = csv.reader(file)
        for row in data:
            csv_content_list.append(row)

    i_not = float(csv_content_list[0][1])
    for i in csv_content_list[1::]:
        result.append([float(i[0]), float(i[1]), round(20*math.log(i_not/float(i[1])), 2)])

    result.append([i_not])
    print(result)

    return result

def display_obs(content):

    clear_frame(content)

    Yscroll = Scrollbar(content)
    Yscroll.pack(side=RIGHT, fill=Y)

    textarea = Text(content, yscrollcommand=Yscroll.set, height=27, width=53)
    Yscroll.config(command=textarea.yview)
    textarea.pack(expand=1, fill=BOTH, padx=50, pady=50)

    words_of_wonders = f"""
AIM ::

\tTo measure the bending loss of the given
\tfiber.


FORMULA USED ::

\tdB = 20 log (Io/I)


RESULT ::

\tGraph shows the bending loss with various
\tbending loop of the fiber.
    """
    textarea.insert(END, words_of_wonders)

def display_graph(graphics, calculation):
    clear_frame(graphics)

    x = [i[0] for i in calculation[:-1]]
    y = [i[2] for i in calculation[:-1]]

    fig = plt.figure(figsize=(4.7, 4.55), dpi=100)
    fig.add_subplot(111).plot(x, y, color="green", linestyle="--")

    plt.title("Bending Loss in the given fiber.")
    plt.xlabel("Bending loop mm")
    plt.ylabel("Loss in dB")

    canvas = FigureCanvasTkAgg(fig, graphics)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, graphics)
    toolbar.update()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

def display_table(graphics, calculation):
    clear_frame(graphics)

    header_names = pd.DataFrame([
    ["Length of", "bending loop", "(mm)"],
    ["Detector", "Current (uA)", ""],
    ["Bending loss", "(dB)", ""]],
    columns = ["S.No", "", ""])

    rows = calculation[:-1]

    print(rows)

    header = pd.MultiIndex.from_frame(header_names)
    index = [i for i in range(1, len(rows)+1)]
    df = pd.DataFrame(rows, columns=header, index=index)

    pt = Table(graphics, dataframe=df, width=410, height=405)
    pt.show()


def display_nav(g_nav, graphics, calculation):

    clear_frame(g_nav)
    clear_frame(graphics)

    display_graph(graphics, calculation)        # default

# displaying the buttons in the graphics navigation pane
    table_button_1 = Button(g_nav, text="Tables", command=lambda: display_table(graphics, calculation))
    table_button_1.pack(side=LEFT)
    graph_button_1 = Button(g_nav, text="Graph 1", command=lambda: display_graph(graphics, calculation))
    graph_button_1.pack(side=LEFT)
    
def main(path, content, graphics, g_nav):
    calculation = solve(path)
    display_obs(content)
    display_nav(g_nav, graphics, calculation)