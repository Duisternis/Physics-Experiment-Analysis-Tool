import csv
import math
from tkinter import *
from pandastable import Table
import pandas as pd
import matplotlib.pylab as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

def clear_frame(frame):
   for widgets in frame.winfo_children():
      widgets.destroy()

def middle_point_cordinate_finder(x, y):
    flag = 0
    max_y = max(y)
    for i in range(len(x)):
        if y[i] > max_y/2 and flag == 0:
            x1 = x[i-1]
            x2 = x[i]
            y1 = y[i-1]
            y2 = y[i]
            flag = 1
        if y[i] < max_y/2 and flag == 1:
            x_1 = x[i-1]
            x_2 = x[i]
            y_1 = y[i-1]
            y_2 = y[i]
            break

    result_x1 = ((max_y/2 - y1)*(x1 - x2)/(y1 - y2)) + x1
    result_x2 = ((max_y/2 - y_1)*(x_1 - x_2)/(y_1 - y_2)) + x_1

    return [[result_x1, max_y/2], [result_x2, max_y/2]]

def solve(path):
    csv_content_list = []
    x_1, x_2, y_1, y_2 = [], [], [], []
    with open(path, "rt") as file:
        data = csv.reader(file)
        for row in data:
            csv_content_list.append(row)

    for i in csv_content_list[1:]:
        if i[1] != '':
            x_1.append(float(i[0]))
            y_1.append(float(i[1]))
        if i[2] != '':
            x_2.append(float(i[0]))
            y_2.append(float(i[2]))
    
    return [x_1, y_1, x_2, y_2, [int(csv_content_list[0][1]), int(csv_content_list[0][2])]]

def display_graph(graphics, calculation):
    clear_frame(graphics)

# seperating x and y co-ordinates to plot them on the graph
    x_1 = calculation[0]
    y_1 = calculation[1]

    x_2 = calculation[2]
    y_2 = calculation[3]

    fig = plt.figure(figsize=(4.7, 4.55), dpi=100)
    fig_plot = fig.add_subplot(111)
    fig_plot.plot(x_1, y_1, color="lightgreen", linestyle="-", label=f"Z = {calculation[-1][0]} mm", marker="o")
    fig_plot.plot(x_2, y_2, color="lightblue", linestyle="-", label=f"Z = {calculation[-1][1]} mm", marker="o")

    
    line_1 = middle_point_cordinate_finder(x_1, y_1)
    line_2 = middle_point_cordinate_finder(x_2, y_2)

    fig_plot.plot([i[0] for i in line_1], [i[1] for i in line_1], color="orange", linestyle="--", marker="p")
    fig_plot.plot([i[0] for i in line_2], [i[1] for i in line_2], color="orange", linestyle="--", marker="p")

    dist_1 = math.sqrt((line_1[0][0] - line_1[1][0])**2 + (line_1[0][1] - line_1[1][1])**2)
    dist_2 = math.sqrt((line_2[0][0] - line_2[1][0])**2 + (line_2[0][1] - line_2[1][1])**2)

    fig_plot.text(line_1[0][0]+dist_1/2.5, line_1[0][1]+1, f"{round(dist_1, 2)} mm", color="red")
    fig_plot.text(line_2[0][0]+dist_2/2.5, line_2[0][1]+1, f"{round(dist_2, 2)} mm", color="red")

    plt.title("Numerical Aperature (N.A) of given fiber.")
    plt.xlabel("Detector Current (I) uA")
    plt.ylabel("Detector Position mm")
    plt.legend(loc="best")

    canvas = FigureCanvasTkAgg(fig, graphics) 
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, graphics)
    toolbar.update()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    return [dist_1, dist_2]

def display_table(graphics, calculation):
    clear_frame(graphics)

    header_names = pd.DataFrame(
        [
        ["Horizontal Position", "of the detector", "across the spot", "'x' mm", ""],
        ["Intensity at varous", "distance from the", "end of the fiber", "'Z' mm", f"Z = {calculation[-1][0]} mm"],
        ["", "", "", "", f"Z = {calculation[-1][1]} mm"]
        ], columns=["S.No", "", "", "", ""]
    )

    rows =[]
    for i in range(len(calculation[2])):
        try: 
            rows.append([calculation[2][i], calculation[1][i], calculation[3][i]])
        except:
            rows.append([calculation[2][i], "", calculation[3][i]])

    print(rows)

    header = pd.MultiIndex.from_frame(header_names)
    index = [i for i in range(1, len(rows)+1)]
    df = pd.DataFrame(rows, columns=header, index=index)

    pt = Table(graphics, dataframe=df, width=400, height=370)
    pt.show()


def display_obs(content, calculation, distance):

    clear_frame(content)

    Yscroll = Scrollbar(content)
    Yscroll.pack(side=RIGHT, fill=Y)

    textarea = Text(content, yscrollcommand=Yscroll.set, height=27, width=53)
    Yscroll.config(command=textarea.yview)
    textarea.pack(expand=1, fill=BOTH, padx=50, pady=50)

    result_1 = math.sin(math.atan(distance[0]/(2*calculation[-1][0])))
    result_2 = math.sin(math.atan(distance[1]/(2*calculation[-1][1])))

    words_of_wonders = f"""
AIM ::
\tTo determine the Numerical Aperture of a\n\tgiven multimode from the measurements\n\ton the far field of the fiber. 


OBSERVATION ::
	
\tNA(1) = sin (θ) 
\t\t= sin ( tan-1 (D/2d))
\t\t= sin ( tan-1 ({round(distance[0], 2)}/(2*{round(calculation[-1][0], 2)}))
\t\t= {round(result_1, 2)}
	
\tNA(1) = sin (θ) 
\t\t= sin ( tan (D/2d))
\t\t= sin ( tan-1 ({round(distance[1], 2)}/(2*{round(calculation[-1][1], 2)}))
\t\t= {round(result_2, 2)}

	
RESULT ::

\tThe numeric Aperture of the given multimode\n\tfiber measured experimentally is {round((result_1+result_2)/2, 2)}.
    
    """
    textarea.insert(END, words_of_wonders)
    
def display_nav(g_nav, graphics, calculation):

    clear_frame(g_nav)
    clear_frame(graphics)

    distance = display_graph(graphics, calculation)        # default

    
    table_button_1 = Button(g_nav, text="Tables", command=lambda: display_table(graphics, calculation))
    table_button_1.pack(side=LEFT)
    graph_button_1 = Button(g_nav, text="Graph 1", command=lambda: display_graph(graphics, calculation))
    graph_button_1.pack(side=LEFT)
    
    return distance

def main(path, content, graphics, g_nav):
    calculation = solve(path)
    print(calculation)
    
    distance = display_nav(g_nav, graphics, calculation)
    display_obs(content, calculation, distance)