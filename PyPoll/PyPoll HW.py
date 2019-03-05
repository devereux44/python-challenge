import os
import csv


csvpath = os.path.join("..", "PyPoll" , "election_data.csv")


with open(csvpath) as csvfile:

    vote_count = []
    candidates = []


    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    
    #Find the number of rows(votes) without the header and set the list of candidates
    for row in csvreader:
        vote_count.append(row[0])

        if candidates not in row:
            candidates.append(row[2])
              
 #Create variables for each time a given candidate's name is voted for and the total percent of votes they have of the total    
Khan_Votes = candidates.count('Khan')
Khan_Percent = round((candidates.count('Khan') / len(vote_count))*100)
Li_Votes = candidates.count('Li')
Li_Percent = round((candidates.count('Li') / len(vote_count))*100)
Correy_Votes = candidates.count('Correy')
Correy_Percent = round((candidates.count('Correy') / len(vote_count))*100)
OTooley_Votes = candidates.count("O'Tooley")
OTooley_Percent = round((candidates.count("O'Tooley") / len(vote_count))*100)

#Print Values
print("Election Results")

print("------------------------")

print(f'Total Votes: {len(vote_count)}')

print("------------------------")

print(f"Khan: {Khan_Percent}% ({Khan_Votes}) ")
print(f"Li: {Li_Percent}% ({Li_Votes}) ")
print(f"Correy: {Correy_Percent}% ({Correy_Votes}) ")
print(f"OTooley: {OTooley_Percent}% ({OTooley_Votes}) ")

print("------------------------")

#Determine who is the winner
if Khan_Votes > Li_Votes:
    print("Khan Wins")
elif Li_Votes > Khan_Votes:
    print("Li Wins")
elif OTooley_Votes > Li_Votes:
    print("OTooley Wins")
elif Correy_Votes > OTooley_Votes:
    print("Correy Wins")


print("------------------------")

# Set variable for output file
output_file = os.path.join("..", "PyPoll", "Output_File.txt")

#  Open the output file
with open(output_file, "w", newline="") as text_file:
    
    print("Election Results", file=text_file)
    print("------------------------", file=text_file)
    print(f'Total Votes: {len(vote_count)}', file=text_file)
    print("------------------------", file=text_file)
    print(f"Khan: {Khan_Percent}% ({Khan_Votes}) ", file=text_file)
    print(f"Li: {Li_Percent}% ({Li_Votes}) ", file=text_file)
    print(f"Correy: {Correy_Percent}% ({Correy_Votes}) ", file=text_file)
    print(f"OTooley: {OTooley_Percent}% ({OTooley_Votes}) ", file=text_file)
    print("------------------------", file=text_file)

    if Khan_Votes > Li_Votes:
        print("Khan Wins", file=text_file)
    elif Li_Votes > Khan_Votes:
        print("Li Wins", file=text_file)
    elif OTooley_Votes > Li_Votes:
        print("OTooley Wins", file=text_file)
    elif Correy_Votes > OTooley_Votes:
        print("Correy Wins", file=text_file)
