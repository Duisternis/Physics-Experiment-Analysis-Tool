import csv
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
    resistance = 0
    csv_content_list = []
    result = []
    with open(path, "rt") as file:
        data = csv.reader(file)
        for row in data:
            csv_content_list.append(row)

    i = 1
    while (csv_content_list[i][0] != "table_end"):
        resistance += float(csv_content_list[i][1])/(0.001*float(csv_content_list[i][2]))
        
        result.append([float(j) for j in csv_content_list[i][1::]] + [float(csv_content_list[i][1])/(0.001*float(csv_content_list[i][2]))])     # V=IR
        i += 1
    
    resistance /= i-1       # average resistance
    i += 1
    
    result.append([[csv_content_list[i][1], csv_content_list[i][2]], csv_content_list[i+1][1], [csv_content_list[i+2][1], csv_content_list[i+2][2]], csv_content_list[i+3][1], csv_content_list[i+4][1], resistance])
    # [ 
    #   [range of ammeter left, right]
    #   least count of ammeter
    #   [range of voltmeter left, right]
    #   least count of voltmeter
    #   length of given wire
    #   resistance
    # ]
    print(result)
    return result

def display_obs(content, calculation):

    clear_frame(content)

    Yscroll = Scrollbar(content)
    Yscroll.pack(side=RIGHT, fill=Y)

    textarea = Text(content, yscrollcommand=Yscroll.set, height=27, width=53)
    Yscroll.config(command=textarea.yview)
    textarea.pack(expand=1, fill=BOTH, padx=50, pady=50)

    words_of_wonders = f"""
Observation ::

    Range of Ammeters\t\t\t\t= {calculation[-1][0][0]}mA to {calculation[-1][0][1]}mA
    Least Count of Ammeter\t\t\t\t= {calculation[-1][1]}mA
    
    Range of Voltmeter\t\t\t\t= {calculation[-1][2][0]}V to {calculation[-1][2][1]}V
    Least count of Voltmeter\t\t\t\t= {calculation[-1][3]}

    Length of the given wire\t\t\t\t= {calculation[-1][4]}cm


Result ::

    Average resistance of wire = {calculation[-1][5]}Ω
    Resistance per unit length of wire 
			= {calculation[-1][5]}Ω / {calculation[-1][4]}cm 
			= {float(calculation[-1][5])/float(calculation[-1][4])}Ω/cm
    
    """
    textarea.insert(END, words_of_wonders)

def display_graph(graphics, calculation):
    clear_frame(graphics)

    x = [i[0] for i in calculation[:-1]]
    y = [i[1] for i in calculation[:-1]]

    fig = plt.figure(figsize=(4.7, 4.55), dpi=100)
    fig.add_subplot(111).plot(x, y, color="green", linestyle="--", label=f"{calculation[-1][5]} Ω")

    plt.title("Resistance Graph (Voltage vs Ampere)")
    plt.xlabel("Voltage (V)")
    plt.ylabel("Current (mA)")
    plt.legend(loc="best")

    canvas = FigureCanvasTkAgg(fig, graphics)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, graphics)
    toolbar.update()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

def display_table(graphics, calculation):
    clear_frame(graphics)

    header_names = pd.DataFrame([
    ["Voltage (V)"],
    ["Current (mA)"],
    ["Resistance (Ω)"]],
    columns = ["S.No"])

    rows = calculation[:-1]

    print(rows)

    header = pd.MultiIndex.from_frame(header_names)
    index = [i for i in range(1, len(rows)+1)]
    df = pd.DataFrame(rows, columns=header, index=index)

    pt = Table(graphics, dataframe=df, width=410, height=450)
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
    display_obs(content, calculation)
    display_nav(g_nav, graphics, calculation)