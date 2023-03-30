from tabulate import tabulate

header = [
    ["S.No", ""],
    ["Readings", "Voltage (V)"],
    ["Readings", "Current (mA)"],
    ["Resistance (Ω)", ""]
]

rows = [
    [1.0, 10.0, 0.1], 
    [2.0, 20.0, 0.1], 
    [3.0, 30.0, 0.1], 
    [4.0, 40.0, 0.1], 
    [5.0, 50.0, 0.1]
]

print(tabulate(rows, headers=header))
