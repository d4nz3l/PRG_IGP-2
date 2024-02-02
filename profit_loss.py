# Import the csv module to work with csv files
import csv

def read_profit_loss(file_path):
    """
    Reads the net profit from a CSV file and stores the data in a list of tuples.
    
    Parameters:
    file_path (str): The path to the CSV file to read.

    Returns:
    List[Tuple[int, float]]: A list of tuples where each tuple contains the day and the net profit for that day.
    """
    profit_loss_data = []
    
    # Open the CSV file and read it using the csv.DictReader
    with open(file_path, 'r', encoding='utf-8-sig') as file:  # Use encoding to handle BOM
        reader = csv.DictReader(file)
        for row in reader:
            day = int(row['Day'])
            net_profit = float(row['Net Profit'])
            profit_loss_data.append((day, net_profit))
    
    return profit_loss_data

def compute_differences(profit_loss_data):
    """
    Computes the daily differences in net profit.
    
    Parameters:
    profit_loss_data (List[Tuple[int, float]]): A list containing the day and net profit for that day.

    Returns:
    List[Tuple[int, float]]: A list of tuples where each tuple contains the day and the difference in net profit from the previous day.
    """
    differences = []
    
    # Using a loop to iterate through the list of net profits to calculate the difference from the previous day.
    for i in range(1, len(profit_loss_data)):
        # Unpacking the current and previous day's profit for readability and ease of difference calculation.
        current_day, current_profit = profit_loss_data[i]
        _, previous_profit = profit_loss_data[i-1]
        # Calculating the difference and appending it as a tuple to maintain a consistent data structure.
        difference = current_profit - previous_profit
        differences.append((current_day, difference))
    
    return differences

def find_extremes(differences):
    """
    Finds the highest increase, highest decrease, or top 3 deficits in net profit.
    
    Parameters:
    differences (List[Tuple[int, float]]): A list containing the day and the difference in net profit.

    Returns:
    Tuple[Tuple[int, float], Tuple[int, float], List[Tuple[int, float]]]: Contains the highest increase, highest decrease, and top 3 deficits in net profit.
    """
    highest_increase = (0, 0)  # Initializing with a base value to be updated.
    highest_decrease = (0, 0)  # Initializing with a base value to be updated.
    deficits = []  # A list to track all deficits.

    # Iterating through each day's difference to find significant changes.
    for day, difference in differences:
        # Updating the highest increase if the current difference is greater than the previously recorded one.
        if difference > highest_increase[1]:
            highest_increase = (day, difference)
        # Updating the highest decrease if the current difference is lower than the previously recorded one.
        elif difference < highest_decrease[1]:
            highest_decrease = (day, difference)
        # Tracking deficits (negative differences) for further analysis.
        if difference < 0:
            deficits.append((day, difference))

    # Sorting the deficits list to prioritize days with the largest deficits.
    # This utilizes a custom sorting function which is defined outside of the lambda scope for simplicity.
    def sort_deficit(item):
        return item[1]
    deficits_sorted = sorted(deficits, key=sort_deficit)

    # Selecting the top 3 deficits by slicing ensures we focus on the days with the most significant losses.
    top_deficits = deficits_sorted[:3]

    return highest_increase, highest_decrease, top_deficits

# Example usage:
# profit_loss_data = read_profit_loss('Profit_and_Loss.csv')
# differences = compute_differences(profit_loss_data)
# highest_increase, highest_decrease, top_deficits = find_extremes(differences)

