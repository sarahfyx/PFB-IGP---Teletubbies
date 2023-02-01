# Import Path function from pathlib 
from pathlib import Path
# Import csv module 
import csv

# setup filepath for reading
fp_read = Path.cwd()/"csv_reports"/"overheads-day-90.csv"

# setup filepath for writing
fp_write = Path.cwd()/"summary_report.txt"

# creating above txt file
fp_write.touch()

# defining the function
def get_highest_overhead():
    """This function reads the overheads-day-90.csv and writes the highest overhead value to the summary_report.txt file."""
    # setting up filepath for reading and writing once again
    fp_read = Path.cwd()/"csv_reports"/"overheads-day-90.csv"
    fp_write = Path.cwd()/"summary_report.txt"
    # creating above txt file
    fp_write.touch()

# creating an empty list
empty_list = []

# open file with .open() to return a file object
with fp_read.open(mode ='r', encoding = "UTF-8", newline = "") as file:
    # create csv reader object using csv
    reader = csv.reader(file)
    # to skip reading header
    next(reader)
    # iterating each row with a for loop
    for row in reader:
        # converting the value in the second row (salary expense) to a float and append it to the empty list
        empty_list.append(float(row[1]))

# assigning the value of the first item in the empty_list to the variable salary_expense
salary_expense = empty_list[0]

# opening the summary_report.txt file for writing
with fp_write.open(mode = "w", encoding = "UTF-8", newline = "") as file:
    # writing the salary expense to the file
    file.write(f"[HIGHEST OVERHEADS] SALARY EXPENSE: {salary_expense}%")

# creating a list for cash surplus and net profit surplus
surplus_data =  ["\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN PREVIOUS DAY"
            "\n[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY"]

# using mode = "a" to append the surplus data to summary_report.txt
with fp_write.open(mode = "a") as file:
    # using writelines method to write multiple lines from surplus_data to summary_report.txt
    file.writelines(surplus_data)

# assigning the value of the seventh item in the empty_list to the variable depreciation_expense
depreciation_expense = empty_list[6]

# using mode = "a" to append the highest overheads (scenario 2) to summary_report.txt
with fp_write.open(mode = "a") as file:
    # using writelines method to write the line for highest overheads (scenario 2) to summary_report.txt
    file.writelines(f"\n\n\n[HIGHEST OVERHEADS] DEPRECIATION EXPENSE: {depreciation_expense}%")





