import tkinter as tk

from pandastable import Table
import pandas as pd

root = tk.Tk()


frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

df = pd.DataFrame()
df["column1"] = [1,2,32342323424342342324342332442323423234423423234999999]
df["column2"] = ["a","b","c"]
df["column3"] = ["a"*100]*3

pt = Table(frame, dataframe=df, width=300)
pt.adjustColumnWidths(limit=30)

pt.show()

root.mainloop()