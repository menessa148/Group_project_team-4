from pathlib import Path
import csv

# Define input and output file paths using pathlib
input_filename = Path.cwd()/"csv_reports"/ "cash on hand.csv.csv"
output_filename = Path.cwd()/"summary_report.txt"

# Function to compute cash deficits and write to the output file
def compute_cash_deficit():
    """
    The function computes cash on hand difference if 
    current day's cash is lower than the previous day's.
    No parameter required.
    """

    # Open the CSV file and read the contents
    with open(input_filename, 'r') as input_file:
        csv_reader = csv.reader(input_file)

        # Skip the header row
        next(csv_reader)  
        
        # Create an empty list to store the "Day" and "Cash on Hand" values
        cash_data = []

        # Read each row in the CSV file and append the "Day" and "Cash on Hand"
        for row in csv_reader:
            day = int(row[0])
            cash_on_hand = int(row[1])
            cash_data.append((day, cash_on_hand))

    # Create a list to store the cash deficits
    cash_deficits = []

    # Check for cash deficit by comparing current day's cash with previous day's cash
    for i in range(1, len(cash_data)):
        if cash_data[i][1] < cash_data[i - 1][1]:
            deficit_amount = cash_data[i - 1][1] - cash_data[i][1]
            cash_deficits.append((cash_data[i][0], deficit_amount))
    
    # Write cash deficits to the output file
    with open(output_filename, 'a') as output_file:
        for day, amount in cash_deficits:
            output_file.write(f"[CASH DEFICIT] DAY: {day}, AMOUNT: USD{amount}\n")

# Calling the function
compute_cash_deficit()