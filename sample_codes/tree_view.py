import pandas as pd
from tkinter import ttk  # for treeview

df = pd.read_excel("F:\\data\\student.xlsx") # create DataFrame

import tkinter as tk

my_w = tk.Tk()
my_w.geometry("500x350")  # width x height
my_w.title("plus2net.com")  # Adding a title

l1 = tk.Label(my_w, text="Search", width=5, font=18)  # added one Label
l1.grid(row=1, column=1, padx=3, pady=10)

e1 = tk.Entry(my_w, width=35, bg="yellow", font=18)  # added one Entry box
e1.grid(row=1, column=2, padx=1)

b1 = tk.Button(my_w, text="Search", width=7, font=18, command=lambda: my_search())
b1.grid(row=1, column=3, padx=2)

def my_search():
    l1 = list(df)  # List of column names as headers
    query = e1.get().strip() # get user entered string
    if query.isdigit():  # if query is number
        str1 = df["id"] == int(query)  #
    else:
        str1 = df.name.str.contains(query, case=False)  # name column value matching
    df2 = df[(str1)]  # combine all conditions using | operator
    r_set = df2.to_numpy().tolist()  # Create list of list using rows
    trv = ttk.Treeview(my_w, selectmode="browse")  # selectmode="browse" or "extended"
    trv.grid(row=2, column=1, columnspan=3, padx=10, pady=20)  #
    trv["height"] = 10  # Number of rows to display, default is 10
    trv["show"] = "headings"
    # column identifiers
    trv["columns"] = l1
    for i in l1:
        trv.column(i, width=90, anchor="c")
        # Headings of respective columns
        trv.heading(i, text=i)
    for dt in r_set:
        v = [r for r in dt]  # creating a list from each row
        trv.insert("", "end", iid=v[0], values=v)  # adding row
my_w.mainloop()