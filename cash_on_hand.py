from pathlib import Path
import csv
# create a file to csv file
fp = Path.cwd()/"project_group"/"csv_reports"/"cash_on_hand.csv"

# create an empty list to store cash on hand by day 
cash_on_hand_list = []

# reads the csv file to append cash on hand from the csv
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    for day, coh in reader:
        # append the data directly to the cash_on_hand_list as a list
        cash_on_hand_list.append([day, coh])

# keeps track of the previous day's cash on hand
previous_day = cash_on_hand_list[0][0]
previous_coh = float(cash_on_hand_list[0][1])