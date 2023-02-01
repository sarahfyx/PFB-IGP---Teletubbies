# Import Path function from pathlib
from pathlib import Path
# Import csv module
import csv


# setup filepath for reading
fp_read = Path.cwd()/"csv_reports"/"profit-and-loss-usd.csv"


# setup filepath for writing
fp_write = Path.cwd()/"summary_report.txt"


# creating above txt file
fp_write.touch()


def profitloss():
    """This function reads the profit-and-loss-usd.csv and writes the profit deficit values to the summary_report.txt file."""
    # setting up filepath for reading and writing once again
    fp_read = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"
    fp_write = Path.cwd()/"summary_report.txt"
    # creating above txt file
    fp_write.touch()


# creating 2 empty lists
empty_list1 = []
empty_list2 = []


# open file with .open() to return a file object
with fp_read.open(mode ='r', encoding = "UTF-8", newline = "") as file:
    # create csv reader object using csv
    reader = csv.reader(file)
    # to skip reading header
    next(reader)
    # iterating each row with a for loop
    for row in reader:
        # converting the value in the first row (day) to a float and append it to the empty list
        empty_list1.append(float(row[0]))
        # converting the value in the fifth row (net profit) to a float and append it to the empty list
        empty_list2.append(float(row[4]))


# assigning the value of the 2nd item (41.0) to day
day = empty_list1[1]


profit_deficit = empty_list2[0] - empty_list2[1]


# using mode = "a" to append the cash deficit (scenario 2) to summary_report.txt
with fp_write.open(mode = "a") as file:
    # using writelines method to write the 2 lines for cash deficit (scenario 2) to summary_report.txt
    file.writelines(f"\n[PROFIT DEFICIT] DAY: {empty_list1[1]}, AMOUNT: USD{profit_deficit}")