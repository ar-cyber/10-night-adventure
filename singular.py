# Imports
from random import *
import openpyxl # pip install openpyxl

# Select the workbook
workbook = openpyxl.load_workbook("80to100.xlsx")
table = workbook.active

# Constants
trials = 100
MODIFIER = 0.3

# Where the trials are stored
b = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}

# Iterate over the amount of trials to run the simulation
for x in range(0, trials):
    a = []
    for y in range(0, 10):
        number = randint(0, 1)
        if number >= MODIFIER: a.append(1)
        else: a.append(0)
    amount = sum(night == 1 for night in a)
    b[amount]+=1

# Output the data into the Excel Spreadsheet
cnt = 0
for row in table.iter_rows(min_row=2, min_col=2):
    col = row[0]
    for col in list(row):
        if cnt > 10:
            continue
        col.value = b[cnt]
        cnt += 1

# Save the data
workbook.save("80to100.xlsx")
