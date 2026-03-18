# Imports
from random import *
import openpyxl # pip install openpyxl

# Load the workbook
workbook = openpyxl.load_workbook("80to100.xlsx")
table = workbook.worksheets[1]

# Constants
trials = 100
m = {0: 0.3, 1: 0.5, 2: 0.7}

# Where the trials are stored
b = {
    0.3: {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0},
    0.5: {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0},
    0.7: {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
}

# Iterate over the modifiers
for modifier in [0.3, 0.5, 0.7]:
    # Iterate over the trials
    for x in range(0, trials):
        a = []
        for y in range(0, 10):
            number = randint(0, 1)
            if number >= modifier: a.append(1)
            else: a.append(0)
        amount = sum(night == 1 for night in a)

        b[modifier][amount]+=1

# Need two counts for this
cnt = 0
cn2 = 0



# Add the data to the spreadsheet
for row in table.iter_rows(min_row=2, max_row=5, min_col=2):
    if cn2 > 2:
        break

    for col in list(row):
        if cnt > 10:
            continue
        col.value = b[m[cn2]][cnt]
        cnt += 1
    cn2+=1
    cnt = 0

# Save the workbook
workbook.save("80to100.xlsx")
