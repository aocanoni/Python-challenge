#os module to let create paths across operating systems?
import os

#module for reading CSV files
import csv

budget_csv = os.path.join('Resources', 'budget_data.csv')

#improved reading using CSV module

with open(budget_csv) as csvfile:

    #csv reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter= ',')
    #skip header row first
    next(csvreader, None)

    #total number of months starting w/0 then gets rewritten later according to # of rows in csv file
    tmonths = 0

    #lists to input months, profits/losses, and changes in profits/losses + averaging them
    months = []

    tamnt = []

    avgchange = []


    for row in csvreader:
        #counts number of rows not including header = number of months (+= means tmonths +1)
        tmonths += 1

        #puts all of the numbers and months into lists
        tamnt.append(int(row[1]))
        months.append(row[0])


    #creates zip of months and tamnt into one list so that I can iterate through it
    budget = list(zip(months, tamnt))

    #initializes all these variables all to 0- will be overwritten
    ginc = 0
    incmonth = 0
    gdec = 0
    decmonth = 0
    
    #this for loop puts the profits/losses all into one list under avgchange
    for num in range(len(tamnt) - 1):
        
        avgchange.append(tamnt[num + 1] - tamnt[num])

    #this for loop goes through the budget list to find the greatest increase/decreasse in profits as well as their corresponding months
    for num in range(len(budget) - 1):

        if (budget[num + 1][1] - budget[num][1]) >= ginc:
            ginc = (budget[num + 1][1] - budget[num][1])
            incmonth = (budget[num + 1][0])

        if (budget[num + 1][1] - budget[num][1]) <= gdec:
            gdec = (budget[num + 1][1] - budget[num][1])
            decmonth = (budget[num + 1][0])




#prints results in terminal
print("                 Financial Analysis               ")
print("--------------------------------------------------") 
print(f"Total Months: {tmonths}")  
#prints the sum of all the numbers in tamnt list
print(f"Total: ${sum(tamnt)}")
print(f"Average Change: ${round((sum(avgchange))/len(avgchange),2)}")
print(f"Greatest Increase in Profits: {incmonth} (${ginc})")
print(f"Greatest Decrease in Profits: {decmonth} (${gdec})")


#Creates text file with results
with open("Analysis/results.txt","w") as file:
    file.write("               Financial Analysis               \n")
    file.write("--------------------------------------------------\n")
    file.write(f"Total Months: {tmonths}\n")
    file.write(f"Total: ${sum(tamnt)}\n")
    file.write(f"Average Change: ${round((sum(avgchange))/len(avgchange),2)}\n")
    file.write(f"Greatest Increase in Profits: {incmonth} (${ginc})\n")
    file.write(f"Greatest Decrease in Profits: {decmonth} (${gdec})\n")
