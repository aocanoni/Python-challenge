#os module to let create paths across operating systems?
import os

#module for reading CSV files
import csv

csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')

#improved reading using CSV module?

with open(csvpath) as csvfile:

    #csv reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter= ',')

    #read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #read each row of dta after the header
    for row in csvreader:
        print(row)

