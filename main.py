import overheads, cash_on_hand, profit_and_loss

# Function to call all the other functions
def main():
    overheads.overhead_function()
    cash_on_hand.compute_cash_deficit()
    profit_and_loss.calculate_profit_deficit()