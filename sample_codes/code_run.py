import csv

with open("content.csv", "rt") as file:
    data = csv.reader(file)
    for row in data:
        print(row)