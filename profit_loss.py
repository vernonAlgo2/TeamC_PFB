from pathlib import Path
import csv
fp = Path.cwd()/"project_group"/"csv_reports"/"MAB CSV"/"profit-and-loss-usd.csv"
# create an empty list to store profit and loss by day
pnl_list = []
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    for day,sales,trading_profit, operating_expense, net_profit in reader:
        # append the data direct to the pnl_list as a list
        pnl_list.append([day, sales, trading_profit, operating_expense, net_profit])