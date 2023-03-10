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

# creating an empty list named overheads
overheads = []

# open file with .open() to return a file object
with fp_read.open(mode ='r', encoding = "UTF-8", newline = "") as file:
    # create csv reader object using csv
    reader = csv.reader(file)
    # to skip reading header
    next(reader)
    # iterating each row with a for loop
    for row in reader:
        # converting the value in the second row (salary expense) to a float and append it to the empty list
        overheads.append(float(row[1]))

# assigning the value of the first item in the empty list to the variable salary_expense
salary_expense = overheads[0]

# opening the summary_report.txt file for writing
with fp_write.open(mode = "w", encoding = "UTF-8", newline = "") as file:
    # writing the highest overhead which is salary expense to the file (scenario 1)
    file.write(f"[HIGHEST OVERHEAD] SALARY EXPENSE: {salary_expense}%")
