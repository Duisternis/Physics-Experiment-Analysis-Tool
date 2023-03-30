import pandas as pd
from IPython.display import display


column_names = pd.DataFrame([["Config", "A"], 
                             ["Config", "B"], 
                             ["Config", "C"], 
                             ["Config", "D"], 
                             ["0th", ""]], 
                             columns=["ID", ""])

rows = [["2", "0", "0", "4", "3"],
        ["0", "0", "0", "0", "4"],
        ["0", "2", "0", "1", "5"]]

columns = pd.MultiIndex.from_frame(column_names)
index = ["0x0", "0x1", "0x2"]

df = pd.DataFrame(rows, columns=columns, index=index)
display(df)