import pandas as pd

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
print(df.to_string())
