import os
import csv
#
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