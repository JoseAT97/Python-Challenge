# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = "C:/Users/Jatab/bootcamp/Homework/Python-Challenge/Starter_Code/PyPoll/Resources/election_data.csv" # Input file path
file_to_output = "C:/Users/Jatab/bootcamp/Homework/Python-Challenge/Starter_Code/Pypoll/analysis/winner_summary.txt"  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidate_votes={}


# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name]= 0

        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    output = ("Election Results\n"
            "-------------------\n"
            f"Total Votes: {total_votes}\n"
            "------------------\n"
    )
            
    

    # Write the total vote count to the text file
    print(output)
    txt_file.write(output)

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes)*100

        # Get the vote count and calculate the percentage
        if votes > winning_count:
            winning_count = votes
            winning_percentage = percentage
            winning_candidate = candidate

        # Print and save each candidate's vote count and percentage
        candidate_output = f"{candidate}: {percentage:3f}% ({votes})\n"
        print(candidate_output, end ="")
        txt_file.write(candidate_output)

    # Generate and print the winning candidate summary
    winner_summary = (
                    "-----------------\n"
                    f"Winner: {winning_candidate}\n"
                    "----------------------------\n"
                    )
    # Save the winning candidate summary to the text file

    print(winner_summary)
    txt_file.write(winner_summary)