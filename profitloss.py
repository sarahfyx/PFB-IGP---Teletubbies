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

# defining the function
def profitloss():
    """This function reads the profit-and-loss-usd.csv and writes the profit deficit
    values (basically means profit increase) to the summary_report.txt file."""
    # setting up filepath for reading and writing once again
    fp_read = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"
    fp_write = Path.cwd()/"summary_report.txt"
    # creating above txt file
    fp_write.touch()


# creating 2 empty lists, day and net_profit
day = []
net_profit = []


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
        # converting the values in the fifth row (net profit) to a float and append it to the empty list
        net_profit.append(float(row[4]))


# assigning the value of the 2nd item (41.0) to day41
day41 = day[1]

# assigning the value of the 5th item (44.0) to day44
day44 = day[4]

# assigning the value of the 9th item (48.0) to day 48
day48 = day[8]

# assigning the value of the 10th item (49.0) to day 49
day49 = day[9]

# assigning the result of subtracting day 41's net profit from day 40's net profit to profit_deficit1
profit_deficit1 = net_profit[0] - net_profit[1]

# assigning the result of subtracting day 44's net profit from day 43's net profit to profit_deficit2
profit_deficit2 = net_profit[3] - net_profit[4]

# assigning the result of subtracting day 48's net profit from day 47's net profit to profit_deficit3
profit_deficit3 = net_profit[7] - net_profit[8]

# assigning the result of subtracting day 49's net profit from day 48's net profit to profit_deficit3
profit_deficit4 = net_profit[8] - net_profit[9]

# using mode = "a" to append the profit deficits to summary_report.txt
with fp_write.open(mode = "a") as file:
    # using writelines method to append the profit deficits to summary_report.txt
    file.writelines(f"\n[PROFIT DEFICIT] DAY: {day41}, AMOUNT: USD{profit_deficit1}"
                    f"\n[PROFIT DEFICIT] DAY: {day44}, AMOUNT: USD{profit_deficit2}"
                    f"\n[PROFIT DEFICIT] DAY: {day48}, AMOUNT: USD{profit_deficit3}"
                    f"\n[PROFIT DEFICIT] DAY: {day49}, AMOUNT: USD{profit_deficit4}")
