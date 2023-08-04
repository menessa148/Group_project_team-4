from pathlib import Path
import csv 


# Create the file paths to the current working directory
input_csv_file = Path.cwd()/"csv_reports"/"profitloss.csv"
output_text_file = Path.cwd()/"summary_report.txt"

def calculate_profit_deficit(input_csv_file, output_text_file):
    # Open the input CSV file
    with open(input_csv_file, newline='') as csvfile:
        # Read the CSV file using the csv.reader
        reader = csv.reader(csvfile)
        # Skip the header row (Day,Sales,Trading Profit,Operating Expense,Net Profit)
        header = next(reader)
        # Initialize a variable to keep track of the day count
        day = 0

        # Open the output text file in write mode
        with open(output_text_file, 'a') as output_file:
            # Iterate through the data (list of lists)
            for row in reader:
                # Increment the day count
                day += 1
                # Convert the 'Net Profit' value for the current day to an integer
                current_net_profit = int(row[4])
                
                # Check if the current day's net profit is less than the previous day
                if day > 1 and current_net_profit < prev_net_profit:
                    # Calculate the deficit amount by subtracting the current day's net profit from the previous day's
                    deficit_amount = prev_net_profit - current_net_profit
                    # Write the deficit information to the output text file
                    output_file.write(f"[PROFIT DEFICIT] DAY: {day}, AMOUNT: USD{deficit_amount}\n")

                # Store the 'Net Profit' value for the current day as previous day's net profit for the next iteration
                prev_net_profit = current_net_profit

# Call the function to calculate and write profit deficits to the output file
calculate_profit_deficit(input_csv_file, output_text_file)