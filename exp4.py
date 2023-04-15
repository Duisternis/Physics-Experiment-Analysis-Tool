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
    global b, t

    csv_content_list = []
    table_1, table_2 = [], []
    with open(path, "rt") as file:
        data = csv.reader(file)
        for row in data:
            csv_content_list.append(row)

    b = float(csv_content_list[-2][1])
    t = float(csv_content_list[-1][1])

    i = 1
    while csv_content_list[i][0] != '-1':
        resistivity = round((float(csv_content_list[i][2])*b*t*1000)/(float(csv_content_list[i][0])*float(csv_content_list[i][1])), 2)
        table_1.append([float(csv_content_list[i][0]), float(csv_content_list[i][1]), float(csv_content_list[i][2]), resistivity])
        i += 1

    i += 2
    while csv_content_list[i][0] != '-1':
        hall_constant = round((float(csv_content_list[i][2])*b*0.001)/(float(csv_content_list[i][1])*float(csv_content_list[i][0])*0.0001), 2)
        table_2.append([float(csv_content_list[i][0]), float(csv_content_list[i][1]), float(csv_content_list[i][2]), hall_constant])
        i += 1

    print([table_1, table_2])

    return [table_1, table_2]

def display_table_1(graphics, calculation):
    clear_frame(graphics)


    header_names = pd.DataFrame([
    ["Current", "(mA)", ""],
    ["Distance", "A -> B", "l (mm)"],
    ["Hall", "Voltage", "(mV)"],
    ["Resistivity", "ρ (Ωm)"]],
    columns = ["S.No", "", ""])

    rows = calculation

    print(rows)

    header = pd.MultiIndex.from_frame(header_names)
    index = [i for i in range(1, len(rows)+1)]
    df = pd.DataFrame(rows, columns=header, index=index)

    pt = Table(graphics, dataframe=df, width=410, height=405)
    pt.show()

def display_table_2(graphics, calculation):
    clear_frame(graphics)

    header_names = pd.DataFrame([
    ["Magnetic", "Field", "B (Gauss)"],
    ["Hall", "Current", "(mA)"],
    ["Hall", "Voltage", "(mV)"],
    ["Hall", "Constant", "(Rh)"]],
    columns = ["S.No", "", ""])

    rows = calculation

    print(rows)

    header = pd.MultiIndex.from_frame(header_names)
    index = [i for i in range(1, len(rows)+1)]
    df = pd.DataFrame(rows, columns=header, index=index)

    pt = Table(graphics, dataframe=df, width=410, height=405)
    pt.show()

def display_nav(g_nav, graphics, calculation):

    clear_frame(g_nav)
    clear_frame(graphics)

    display_graph(graphics, calculation[0])        # default

# displaying the buttons in the graphics navigation pane
    table_button_1 = Button(g_nav, text="Table 1", command=lambda: display_table_1(graphics, calculation[0]))
    table_button_1.pack(side=LEFT)
    table_button_2 = Button(g_nav, text="Table 2", command=lambda: display_table_2(graphics, calculation[1]))
    table_button_2.pack(side=LEFT)
    graph_button_1 = Button(g_nav, text="Graph 1", command=lambda: display_graph(graphics, calculation[0]))
    graph_button_1.pack(side=LEFT)
    
def display_graph(graphics, calculation):
    clear_frame(graphics)

    x = [i[0] for i in calculation]
    y = [i[2] for i in calculation]

    fig = plt.figure(figsize=(4.7, 4.55), dpi=100)
    fig.add_subplot(111).plot(x, y, color="green", linestyle="--")

    plt.title("Hall Voltage v/s Current")
    plt.xlabel("I (mA)")
    plt.ylabel("V (mV)")

    canvas = FigureCanvasTkAgg(fig, graphics)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, graphics)
    toolbar.update()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

def display_obs(content, calculation):

    clear_frame(content)

    Yscroll = Scrollbar(content)
    Yscroll.pack(side=RIGHT, fill=Y)

    textarea = Text(content, yscrollcommand=Yscroll.set, height=27, width=53)
    Yscroll.config(command=textarea.yview)
    textarea.pack(expand=1, fill=BOTH, padx=50, pady=50)

    rh, b_ = 0, 0
    for i in calculation[1]:
        rh += i[3]
        b += i[0]
    rh /= len(calculation[1])
    b /= len(calculation[1])
    rh = round(rh, 2)
    b = round(b, 2)

    rho = 0
    for i in calculation[0]:
        rho += i[3]
    rho /= len(calculation[0])
    rho = round(rho, 2)

    mu = rh/rho

    n = round(1/(1.6*rh), 2)

    angle = round(math.tan(mu*b_), 2)

    words_of_wonders = f"""
AIM ::

\t1. To study the Hall effect and to determine
\t\t(i) Hall Voltage
\t\t(ii) Hall Coefficient
\t2. Whether the semiconductor is n-type or 
\tp-type
\t3. Hall angle.

FORMULA USED & CALCULATIONS :: 

\tWidth of the specimen,\t’b’ = {b} mm
\tLength of the specimen,\t’l’ = {calculation[0][0][1]} mm
\tThickness of the specimen,\t’t’ = {t}mm

\tRh = (Vh x b) / (I x B)
\t\t= {rh} m^3 C^-1

\t Sign of hall coefficient is +ve
\t so the semi-conductor is of p-type.

\tResistivity (ρ) = (Vh x b x t) / (l)
\t\t= {rho} Ω m

\tn = 1/(e x Vh) 
\t\t= {n} x 10^19 carriers per m^3

\tMobility (u) = Rh/ρ
\t\t= {mu} 
\t\tm^2 V^-1 s^-1

\tHall angle = tan^-1(uB)
\t\t= {angle}

RESULT ::

\tHall effect is studied and verified.
    """
    textarea.insert(END, words_of_wonders)

def main(path, content, graphics, g_nav):
    calculation = solve(path)
    display_obs(content, calculation)
    display_nav(g_nav, graphics, calculation)