#os module to let create paths across operating systems?
import os

#module for reading CSV files
import csv

#ask if ".." needs to be added- it doesn't work when I add in front of resources? likely because main.py is in the same folder as Resources?
budget_csv = os.path.join('Resources', 'budget_data.csv')

#improved reading using CSV module??

with open(budget_csv) as csvfile:

    #csv reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter= ',')
    #skip header row first
    next(csvreader, None)

    #total number of months starting w/0 then gets rewritten according to # of rows in csv file
    tmonths = 0

    #list that profit/losses will be added to for total amount
    months = []

    tamnt = []

    avgchange = []


    for row in csvreader:
        #counts number of rows not including header = number of months (+= means tmonths +1)
        tmonths += 1

        #puts all of the numbers into a list
        tamnt.append(int(row[1]))
        months.append(row[0])


    budget = list(zip(months, tamnt))
    ginc = 0
    incmonth = 0
    gdec = 0
    decmonth = 0
    
    for num in range(len(tamnt) - 1):
        
        avgchange.append(tamnt[num + 1] - tamnt[num])

    for num in range(len(budget) - 1):

        if (budget[num + 1][1] - budget[num][1]) >= ginc:
            ginc = (budget[num + 1][1] - budget[num][1])
            incmonth = (budget[num + 1][0])

        if (budget[num + 1][1] - budget[num][1]) <= gdec:
            gdec = (budget[num + 1][1] - budget[num][1])
            decmonth = (budget[num + 1][0])





    print("                 Financial Analysis               ")
    print("--------------------------------------------------") 
    print(f"Total Months: {tmonths}")
    
    #prints the sum of all the numbers in tamnt list
    print(f"Total: ${sum(tamnt)}")
    print(f"Average Change: ${round((sum(avgchange))/len(avgchange),2)}")
    print(f"Greatest Increase in Profits: {incmonth} (${ginc})")
    print(f"Greatest Decrease in Profits: {decmonth} (${gdec})")



with open("Analysis/results.txt","w") as file:
    file.write("               Financial Analysis               \n")
    file.write("--------------------------------------------------\n")
    file.write(f"Total Months: {tmonths}\n")
    file.write(f"Total: ${sum(tamnt)}\n")
    file.write(f"Average Change: ${round((sum(avgchange))/len(avgchange),2)}\n")
    file.write(f"Greatest Increase in Profits: {incmonth} (${ginc})\n")
    file.write(f"Greatest Decrease in Profits: {decmonth} (${gdec})\n")
