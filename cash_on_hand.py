# Import the csv module to work with CSV files. The CSV module provides functionality to both read from and write to CSV files.
import csv

def read_cash_on_hand(file_path):
    """
    This function opens a CSV file containing cash on hand data and converts it into a list of tuples.
    Each tuple represents the cash on hand for a given day. By reading the file this way, we create
    a structured representation of the CSV in memory, which can be easily manipulated with Python.

    Parameters:
    file_path (str): The path to the CSV file to read.

    Returns:
    List[Tuple[int, float]]: A list where each tuple contains two elements:
                             the first element is an integer representing the day, and
                             the second element is a float representing the cash on hand.
    """
    cash_data = []  # Initialize an empty list to store the cash on hand data.
    
    # Open the file using a context manager, which ensures the file is properly closed after its block is exited.
    # The 'utf-8-sig' encoding is used to handle files with a BOM (Byte Order Mark).
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)  # The DictReader object translates each row of the file into a dictionary.
        for row in reader:
            # The dictionary keys correspond to the header names of the CSV file. We ensure these keys are exactly matched.
            day = int(row['Day'])  # Convert the 'Day' column to an integer.
            cash_on_hand = float(row['Cash On Hand'])  # Convert the 'Cash On Hand' column to a float.
            cash_data.append((day, cash_on_hand))  # Append a tuple of (day, cash_on_hand) to the cash_data list.
    
    return cash_data  # Return the list of tuples.

def compute_differences(cash_data):
    """
    This function calculates the day-to-day differences in cash on hand. It demonstrates the ability to perform
    numerical computations and work with sequential data, iterating over the list with awareness of previous elements.

    Parameters:
    cash_data (List[Tuple[int, float]]): The cash on hand data as a list of tuples.

    Returns:
    List[Tuple[int, float]]: A list of tuples where each tuple contains the day and the calculated difference
                             in cash on hand from the previous day.
    """
    differences = []  # Initialize an empty list to store the daily differences in cash on hand.
    
    # Iterate through the list of cash on hand data starting from the second element.
    for i in range(1, len(cash_data)):
        # Calculate the difference by subtracting the previous day's cash on hand from the current day's.
        difference = cash_data[i][1] - cash_data[i-1][1]
        # Append a tuple of (current day, difference) to the differences list.
        differences.append((cash_data[i][0], difference))
    
    return differences  # Return the list of daily differences.

def find_extremes(differences):
    """
    This function identifies the days with the highest increase and decrease in cash on hand,
    as well as the top three deficits. This showcases how to analyze financial data to extract
    meaningful insights, such as identifying the best and worst performing days.

    Parameters:
    differences (List[Tuple[int, float]]): The list of daily cash on hand differences.

    Returns:
    Tuple[Tuple[int, float], Tuple[int, float], List[Tuple[int, float]]]: A tuple containing the highest increase,
                                                                            the highest decrease, and the list of the top
                                                                            three deficits in cash on hand.
    """
    highest_increase = (0, 0)  # Initialize the highest increase as a tuple with a placeholder value.
    highest_decrease = (0, 0)  # Initialize the highest decrease similarly.
    deficits = []  # Initialize an empty list to store days with cash deficits.

    # Loop through each day's cash change to find the extremes.
    for day, difference in differences:
        # If the current day's change is greater than the current highest increase, update highest_increase.
        if difference > highest_increase[1]:
            highest_increase = (day, difference)
        # If the current day's change is less than the current highest decrease, update highest_decrease.
        elif difference < highest_decrease[1]:
            highest_decrease = (day, difference)
        
        # If there's a deficit (negative change), add the day and amount to the deficits list.
        if difference < 0:
            deficits.append((day, difference))
    
    # Define a function to be used as a key for sorting the deficits
    # Sort the deficits list by the deficit amount in ascending order using a custom sorting function
    def deficit_sort(deficit):
        return deficit[1]  # We return the second item in the tuple (the deficit amount) for sorting

    deficits.sort(key=deficit_sort)
    # Get the top 3 deficits
    top_deficits = deficits[:3]

    return highest_increase, highest_decrease, top_deficits

# Example usage:
# cash_data = read_cash_on_hand('Cash_on_Hand.csv')
# differences = compute_differences(cash_data)
# highest_increase, highest_decrease, top_deficits = find_extremes(differences)

