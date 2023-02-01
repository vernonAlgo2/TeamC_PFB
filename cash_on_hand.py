from pathlib import Path

import csv

# create a file to csv file

fp = Path.cwd()/"project_group"/"csv_reports"/"MAB CSV"/"45-overheads.csv"



# create an empty list to store overhead

overhead_list = []

with fp.open(mode="r", encoding="UTF-8", newline="") as file:

    reader = csv.reader(file)

    next(reader)

    for expense, percentage in reader:

        # append the data directly to the overhead_list as a list

        overhead_list.append([expense, percentage])




# Assign the first category and percentage from the list as the initial highest

# Set as a reference point for the next elements in the list

highest_category = overhead_list[0][0]

highest_percentage = float(overhead_list[0][1])