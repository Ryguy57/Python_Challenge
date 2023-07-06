# Python_Challenge
Week 3

PyBank


import os
import csv
budget_csv = os.path.join("Resources", "budget_data.csv")
Months =[]
Profit_loss = []
with open(budget_csv) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for item in csvreader:
        Months.append(item[0])
        Profit_loss.append(item[1])
    Profit_loss = [int(i) for i in Profit_loss]
monthly_profit_change = []

 

Total_Months = len(Months)
Total_Profit = sum(Profit_loss)
Avg_Difference = round ((Profit_loss[-1] - Profit_loss[0]) / ((Total_Months)- 1),2)

monthly_profit_change = []
for i in range(len(Profit_loss) - 1):
    monthly_profit_change.append(Profit_loss[i + 1] - Profit_loss[i])
max_increase_value = max(monthly_profit_change)
max_increase_index = monthly_profit_change.index(max_increase_value)
max_increase_month = Months[max_increase_index + 1]

max_decrease_value = min(monthly_profit_change)
max_decrease_index = monthly_profit_change.index(max_decrease_value)
max_decrease_month = Months[max_decrease_index + 1]

print(f'Financial Analysis')
print(f'-------------------------')
print(f'Total Months: {Total_Months}')
print(f'Total:  ${Total_Profit}')
print(f'Average Change: {Avg_Difference}')
print(f"Greatest Increase in Profits: {max_increase_month} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {max_decrease_month} (${(str(max_decrease_value))})")


output = (f'Financial Analysis\n'
f'-------------------------\n'
f'Total Months: {Total_Months}\n'
f'Total:  ${Total_Profit}\n'
f'Average Change: ${Avg_Difference}\n'
f"Greatest Increase in Profits: {max_increase_month} (${(str(max_increase_value))})\n"
f"Greatest Decrease in Profits: {max_decrease_month} (${(str(max_decrease_value))})\n")
# Set variable for output file
output_file = os.path.join("Analysis","budget_final.txt")
#  Open the output file
with open(output_file, "w") as txt_file:
    txt_file.write(output)


PyPoll

import os
import csv

election_csv = os.path.join( "Resources", "election_data.csv")


# Create empty lists to store candidate information
candidate_names = []
total_votes = []
vote_percentages = []

# Read data from CSV file
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip header row

    # Create dictionary to store vote counts for each candidate
    candidates = {}

    # Count votes for each candidate
    for row in csvreader:
        candidate = row[2]

        # If candidate is not in the dictionary, add them with initial vote count of 1
        if candidate not in candidates:
            candidates[candidate] = 1
        else:
            candidates[candidate] += 1

    # Calculate total votes
    total_vote_count = sum(candidates.values())
    print(total_vote_count)

    # Calculate candidate information
    for candidate, vote_count in candidates.items():
        vote_percentage = round(((vote_count / total_vote_count) * 100),3)
        #formatted_percentage = '{:.3f}%'.format(vote_percentage)
        #formatted_vote_count = '{:,}'.format(vote_count)
       
        # Append candidate information to the lists
        candidate_names.append(candidate)
        total_votes.append(vote_count)
        vote_percentages.append(vote_percentage)

# Display the candidate information
for i in range(len(candidate_names)):
    print(f'{candidate_names[i]}: {vote_percentages[i]}% ({total_votes[i]})')

# Find the candidate with the most votes
winner = max(candidates, key=candidates.get)

# Print the name of the candidate with the most votes
output = (f'\n'
f'Election Results\n'
f'-------------------------\n'
f'Total Votes: {total_votes}\n'
f'-------------------------\n'
f'{candidate_names[0]}: {vote_percentages[0]}% ({total_votes[0]})\n'
f'{candidate_names[1]}: {vote_percentages[1]}% ({total_votes[1]})\n'
f'{candidate_names[2]}: {vote_percentages[2]}% ({total_votes[2]})\n'
f'-------------------------\n'
f'Winner: {winner}\n')
output_file = os.path.join("analysis","election_final.txt")
with open(output_file, "w") as txt_file:
    txt_file.write(output)


    Cited Peer Collaberation with Adam Gostinger, Juliet Hamilton and Jennifer Grubbs
