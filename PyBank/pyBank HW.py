import os

import csv

csvpath = os.path.join("..", "PyBank", "budget_data.csv")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    profit = []
    date = []
    total = []
    greatestchange = []

       
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    #Count the number of rows without the header
    for row in csvreader:
        date.append(row[0])
        profit.append(float(row[1]))

    #Print the header, page break, total number of months, and the total profit
    print('Financial Analysis')
    print('------------------')
    print(f'Total Months: {len(date)}')
    print(f'Total Profit: ${int(sum(profit))}')
    
    #Create a 0 value to find the change in profit from one month to another
    x = 0
    for x in range(1,len(profit)):
        greatestchange.append(profit[x] - profit[x-1])

    #Find the average, max, and min of the Month over Month change
    print(f'Average Change: ${round(sum(greatestchange)/len(greatestchange))}')  
    print(f'Greatest Increase: ${round(max(greatestchange))}')
    print(f'Greatest Decease: ${round(min(greatestchange))}')  


# Set variable for output file
output_file = os.path.join("..", "PyBank", "Output_File.txt")

#  Open the output file
with open(output_file, "w", newline="") as text_file:
    
    #print the table into the text file
    print(f'Financial Analysis', file=text_file)
    print(f'------------------', file=text_file)
    print(f'Total Months: {len(date)}', file=text_file)
    print(f'Total Profit: ${int(sum(profit))}', file=text_file)
    print(f'Average Change: ${round(sum(greatestchange)/len(greatestchange))}', file=text_file)  
    print(f'Greatest Increase: ${round(max(greatestchange))}', file=text_file)
    print(f'Greatest Decease: ${round(min(greatestchange))}', file = text_file)


