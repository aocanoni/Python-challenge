#os module to let create paths across operating systems?
import os

#module for reading CSV files
import csv

#ask if ".." needs to be added- it doesn't work when I add in front of resources? likely because main.py is in the same folder as Resources?
csvpath = os.path.join('Resources', 'budget_data.csv')


#variables for budget_data

#improved reading using CSV module?

with open(csvpath) as csvfile:

    #csv reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter= ',')

    #print(csvreader)

    #read the header row first
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #read each row of dta after the header
    for row in csvreader:
        #print(row)

