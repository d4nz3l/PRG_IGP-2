# # main.py

# Import necessary functions from the cash_on_hand, overheads, and profit_loss modules.
# These functions are essential for reading and processing financial data.
from cash_on_hand import read_cash_on_hand, compute_differences as compute_cash_differences, find_extremes as find_cash_extremes
from overheads import read_overheads, find_highest_overhead
from profit_loss import read_profit_loss, compute_differences as compute_profit_differences, find_extremes as find_profit_extremes

# A function to sort a list of tuples based on the second item in each tuple.
def sort_by_amount(item):
    # Returns the second element of the tuple for sorting purposes.
    return item[1]

def generate_summary_report():
    """
    The core function of this module. It integrates and synthesizes data from various financial reports
    to generate a coherent and comprehensive summary of a company's financial activities.
    The output is a text file that provides clear and actionable insights into the company's financial health.
    """
    # Read and analyze the cash on hand data from the corresponding CSV file.
    # This involves calculating daily differences and identifying any extremes, such as deficits.
    cash_data = read_cash_on_hand('csv_reports/cash_on_hand.csv')
    cash_differences = compute_cash_differences(cash_data)
    cash_increase, cash_decrease, cash_deficits = find_cash_extremes(cash_differences)
    
    # Read and determine the highest overhead from the overheads CSV file.
    # This information is crucial for understanding cost structures and identifying potential savings.
    overheads_data = read_overheads('csv_reports/Overheads.csv')
    highest_overhead = find_highest_overhead(overheads_data)
    
    # Read and analyze profit and loss data from the corresponding CSV file.
    # This helps in understanding the profitability trends and identifying any problem areas.
    profit_loss_data = read_profit_loss('csv_reports/Profit_and_Loss.csv')
    profit_differences = compute_profit_differences(profit_loss_data)
    profit_increase, profit_decrease, profit_deficits = find_profit_extremes(profit_differences)
    
    # Open (or create if it doesn't exist) the summary report file in write mode.
    with open('summary_report.txt', 'w') as file:
        # Write the highest overhead category and amount to the summary report.
        # This gives a quick snapshot of the most significant expense the company is incurring.
        file.write(f"[HIGHEST OVERHEAD] {highest_overhead['category'].upper()}: {highest_overhead['overhead']}%\n\n")

        # Analyze cash on hand trends to determine if there is a consistent surplus or deficit.
        consistent_cash = all(difference >= 0 for _, difference in cash_differences)
        # Similarly, analyze profit trends to determine if there is a consistent surplus or deficit.
        consistent_profit = all(difference >= 0 for _, difference in profit_differences)
        
        # If there's a consistent cash surplus, write only the highest surplus to the report.
        # This simplifies the report for readers, providing a clear indicator of financial health.
        if consistent_cash:
            file.write(f"[HIGHEST CASH SURPLUS] DAY: {cash_increase[0]}, AMOUNT: USD{cash_increase[1]}\n\n")
        else:
            # If the cash trend is fluctuating, list all days with cash deficits.
            # This detailed breakdown helps identify specific days which contributed most to the deficit.
            for day, deficit in cash_differences:
                if deficit < 0:
                    file.write(f"[CASH DEFICIT] DAY: {day}, AMOUNT: USD{abs(deficit)}\n")
            file.write("\n")
            # Additionally, highlight the top 3 days with the highest cash deficits for quick reference.
            cash_deficits_sorted = sorted(cash_deficits, key=sort_by_amount)[:3]
            for i, (day, deficit) in enumerate(cash_deficits_sorted, start=1):
                ordinal = ["1ST", "2ND", "3RD"][i - 1]
                file.write(f"[{ordinal} HIGHEST CASH DEFICIT] DAY: {day}, AMOUNT: USD{abs(deficit)}\n")
            file.write("\n")
        
        # Write Profit and Loss results
        if consistent_profit:
         # If the profit trend is consistent, we utilize conditional logic to decide what to write to the file.
         # Here, we use string formatting to construct a message that includes the day and the amount
         # which represents the highest net profit surplus.
            file.write(f"[HIGHEST NET PROFIT SURPLUS] DAY: {profit_increase[0]}, AMOUNT: USD{profit_increase[1]}\n\n")
        else:
         # For fluctuating profit data, we iterate over each day's profit differences using a for loop.
         # This loop, combined with a conditional statement, checks for and writes out each deficit.
            for day, deficit in profit_differences:
                if deficit < 0:
                    # The abs() function is applied to format the deficit as a positive number for the report.
                    file.write(f"[NET PROFIT DEFICIT] DAY: {day}, AMOUNT: USD{abs(deficit)}\n")
            file.write("\n")
            

            # We sort the list of deficits to find the days with the largest deficits.
            profit_deficits_sorted = sorted(profit_deficits, key=sort_by_amount)[:3]
            for i, (day, deficit) in enumerate(profit_deficits_sorted, start=1):
                # We use enumerate in the for loop to get both the index and deficit amount.
                # The index is used to determine the ordinal ranking (1st, 2nd, 3rd) for the report.
                ordinal = ["1ST", "2ND", "3RD"][i - 1]
                file.write(f"[{ordinal} HIGHEST NET PROFIT DEFICIT] DAY: {day}, AMOUNT: USD{abs(deficit)}\n")
            file.write("\n")
        # Write Profit and Loss results

# Execute the report generation
generate_summary_report()



        

