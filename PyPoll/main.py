import os
import csv

election_csv = os.path.join('Resources', 'election_data.csv')

with open(election_csv) as csvfile:

    csvreader = csv.reader(csvfile, delimiter= ',')
 
    next(csvreader, None)
 
    #total number of votes
    tvotes = 0

    #complete list of all candidates including duplicates
    lnames = []

    for row in csvreader:
        tvotes += 1

        #using row[2] from csv to get names to put into lnames list
        lnames.append(row[2])

    #turn lnames into a set to get unique names
    Snames = set(lnames)
    #turn Snames into list to get list of unique names
    names = list(Snames)
    
    #counter of votes for each person
    person1 = 0
    person2 = 0
    person3 = 0

    #winner will be rewritten depending on who has largest number of votes
    winner = 0

    for name in lnames:

        #if statements to get total num of votes for each name
        if name == names[0]:
            person1 += 1

        if name == names[1]:
            person2 += 1
 
        if name == names[2]:
            person3 += 1

    #If statement to get highest num of votes to indicate person for winner
    if (person1 > person2) and (person1 > person3):
        winner = names[0]
    elif (person2 > person1) and (person2 > person3):
        winner = names[1]
    else:
        winner = names[2]

    #get percent: votes for each person/total number of votes
    perc1 = round((person1/tvotes) * 100,3)
    perc2 = round((person2/tvotes) * 100,3)
    perc3 = round((person3/tvotes) * 100,3)
    

    
print("               Election Results               ")
print("----------------------------------------------") 
print(f"Total Votes: {tvotes}")
print("----------------------------------------------")
print(f"{names[0]}: {perc1}% ({person1})")
print(f"{names[1]}: {perc2}% ({person2})")
print(f"{names[2]}: {perc3}% ({person3})")
print("----------------------------------------------")
print(f"Winner: {winner}")
print("----------------------------------------------")


with open("Analysis/results.txt","w") as file:
    file.write("               Election Results               \n")
    file.write("----------------------------------------------\n")
    file.write(f"Total Votes: {tvotes}\n")
    file.write("----------------------------------------------\n")
    file.write(f"{names[0]}: {perc1}% ({person1})\n")
    file.write(f"{names[1]}: {perc2}% ({person2})\n")
    file.write(f"{names[2]}: {perc3}% ({person3})\n")
    file.write("----------------------------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("----------------------------------------------\n")