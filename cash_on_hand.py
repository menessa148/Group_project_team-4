from pathlib import Path
import csv

# Define the file path
fp = Path.cwd()/"csv_reports"/"cash on hand.csv.csv"

# Open the CSV file and read its contents
with fp.open(mode= "r", encoding="UTF-8") as file:
    reader = csv.reader(file)

    # Skip the header row
    next(reader)

    # Create a list to store the "Day" ans "Cash on hand" values
    coh = []

    # Read each row in the CSV file and append the "Day" and "Cash on hand"
    for row in reader:
        coh.append([row[0], row[1]])

# Define a function to calculate deficits for each day
def calculate_deficit(coh):
    deficits = []

    # Calculate the deficit for each day
    for current in range(1, len(coh)):
        prev_day_cash = int(coh[current - 1][1])
        current_day_cash = int(coh[current][1])
        deficit = prev_day_cash - current_day_cash
        deficits.append(deficit)

    return deficits

# Call the function to calculate deficits and store the results in deficits_list
deficits_list = calculate_deficit(coh)

# Print the deficits for each day
for day, deficit in enumerate(deficits_list):
    print(f"Day {day + 1}, Deficit: {deficit}")