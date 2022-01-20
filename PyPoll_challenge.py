import csv
import os
#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Create empty candidate list and dictonary 
candidate_options = []
candidate_votes = {}
 # Create a county list and county votes dictionary.
county_list = []
county_votes = {}

# Winning candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Track the largest county and county voter turnout.
largest_county = ""
largest_county_turnout = 0
c_winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:
    
# To do: read and analyze the data here.    
    file_reader = csv.reader(election_data)
    
    # Read the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total votes count
        total_votes += 1

    # Print the candidate name from each row.
        candidate_name = row[2]
    # Extract the county name from each row.
        county_name = row[1]
    
    # If the candidate does not match an existing candidate:
        if candidate_name not in candidate_options:

        # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
        
        # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

    # Write an if statement that checks that the county does not match any existing county in the county list.
        if county_name not in county_list:

        #  Add the existing county to the list of counties
            county_list.append(county_name)
        
        # Begin tracking county's vote count
            county_votes[county_name] = 0

        # Add a vote to that county's vote count
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)    

# Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
    # Retrieve vote count
        c_votes = county_votes[county_name]
    # Calculate the percentage of votes
        c_vote_percentage = float(c_votes) / float(total_votes) * 100
    # Print each county, their voter count, and percentage to the terminal.
        county_results = (
            f"{county_name}: {c_vote_percentage:.1f}% ({c_votes:,})\n")

        print(county_results)
    # Save the candidate results to our text file.
        txt_file.write(county_results)

    # Determine winning vote and candidate, as well as  if votes is greater than the winning count.
        if (c_vote_percentage > c_winning_percentage):
    # If true then set winning_count = votes and winning_percent = vote_percentage
            c_winning_percentage = c_vote_percentage
    # And, set the winning_candidate equal to the candidate's name
            largest_county = county_name

    largest_county_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"-------------------------\n")
    print(largest_county_summary)
# Save the winning candidate's results to the text file.
    txt_file.write(largest_county_summary)

# Determine the percentage of votes for each candidate by looping through the counts. Then iterate through the candidate list.
    for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
    # Print each candidate, their voter count, and percentage to the terminal.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
    # Save the candidate results to our text file.
        txt_file.write(candidate_results)

# Determine winning vote and candidate, as well as  if votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
    # If true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
    # And, set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
# Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)