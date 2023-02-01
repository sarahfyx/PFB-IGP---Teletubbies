# Import Path function from pathlib
from pathlib import Path
# Import csv module
import csv

# setup filepath for reading
fp_read = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"

# setup filepath for writing
fp_write = Path.cwd()/"csv_reports"/"summary_report.txt"

# creating above txt file
fp_write.touch()


def cashonhand():
    """This function reads the cash-on-hand.csv and writes the highest overhead value to the summary_report.txt file."""
    # setting up filepath for reading and writing once again
    fp_read = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"
    fp_write = Path.cwd()/"summary_report.txt"
    # creating above txt file
    fp_write.touch()


# creating an empty list
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
        # converting the value in the third row (Day 41) to a float and append it to the empty list
        empty_list1.append(float(row[0]))
        empty_list2.append(float(row[1]))


# assigning the value of the 2nd item (41.0) to day_1
day_1 = empty_list1[1]
# assigning the result of subtracting day 41's value from day 40 to cash_deficit1
cash_deficit1 = empty_list2[0] - empty_list2[1]
# assigning the value of the 9th item (48.0) to day_2
day_2 = empty_list1[8]
# assigning the result of subtracting day 48's value from day 47 to cash_deficit1
cash_deficit2 = empty_list2[7] - empty_list2[8]


# using mode = "a" to append the cash deficit (scenario 2) to summary_report.txt
with fp_write.open(mode = "a") as file:
    # using writelines method to write the 2 lines for cash deficit (scenario 2) to summary_report.txt
    file.writelines(f"\n[CASH DEFICIT] DAY: {empty_list1[1]} , AMOUNT: USD{cash_deficit1}"
    f"\n[CASH DEFICIT] DAY: {empty_list1[8]} , AMOUNT: USD{cash_deficit2}")