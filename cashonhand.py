# Import Path function from pathlib
from pathlib import Path
# Import csv module
import csv

# setup filepath for reading
fp_read = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"

# setup filepath for writing
fp_write = Path.cwd()/"summary_report.txt"

# creating above txt file
fp_write.touch()

# defining the function
def cashonhand():
    """This function reads the cash-on-hand.csv and writes the cash deficit 
    values (basically means increase in cash on hand) to the summary_report.txt file."""
    # setting up filepath for reading and writing once again
    fp_read = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"
    fp_write = Path.cwd()/"summary_report.txt"
    # creating above txt file
    fp_write.touch()

# creating 2 empty lists, day and coh
day = []
coh = []

# open file with .open() to return a file object
with fp_read.open(mode ='r', encoding = "UTF-8", newline = "") as file:
    # create csv reader object using csv
    reader = csv.reader(file)
    # to skip reading header
    next(reader)
    # iterating each row with a for loop
    for row in reader:
        # converting the values in the first row (day) to a float and append it to the empty list
        day.append(float(row[0]))
        # converting the values in the second row (cash on hand) to a float and append it to the empty list
        coh.append(float(row[1]))


# assigning the value of the 2nd item (41.0) to day41
day41 = day[1]

# assigning the value of the 5th item (44.0) to day44
day44 = day[4]

# assigning the value of the 9th item (48.0) to day48
day48 = day[8]

# assigning the result of subtracting day 41's cash on hand value from day 40's value on to cash_deficit1
cash_deficit1 = coh[0] - coh[1]

# assigning the result of subtracting day 44's cash on hand value from day 43 to cash_deficit2
cash_deficit2 = coh[3] - coh[4]

# assigning the result of subtracting day 48's cash on hand value from day 47 to cash_deficit3
cash_deficit3 = coh[7] - coh[8]

# using mode = "a" to append the cash deficits to summary_report.txt
with fp_write.open(mode = "a") as file:
    # using writelines method to append the 3 lines for cash deficit to summary_report.txt
    file.writelines(f"\n[CASH DEFICIT] DAY: {day41}, AMOUNT: USD{cash_deficit1}"
    f"\n[CASH DEFICIT] DAY: {day44}, AMOUNT: USD{cash_deficit2}"
    f"\n[CASH DEFICIT] DAY: {day48}, AMOUNT: USD{cash_deficit3}")