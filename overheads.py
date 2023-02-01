


















for expense in overhead_list:
    # Check if the current expense's percentage is greater than the current highest percentage
    if float(expense[1]) > highest_percentage:
    # Update the highest category and highest percentage if the current expense's category and percentage is greater than the previous high
        highest_category = expense[0]
        highest_percentage = float(expense[1])
# create the summary_report text file
fp_cwd = Path.cwd()/"summary_report.txt"
fp_cwd.touch()
# opens the file to write the output
with fp_cwd.open(mode="w", encoding = "UTF-8", newline ="") as file:
    file.write(f"[HIGHEST OVERHEADS]{highest_category.upper()}: {highest_percentage}%\n")
