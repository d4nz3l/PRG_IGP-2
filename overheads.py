# Import the csv module to work with csv files
import csv

def read_overheads(file_path):
    """
    Reads the overheads from a CSV file and stores the data in a list of dictionaries.
    
    Parameters:
    file_path (str): The path to the CSV file to read.

    Returns:
    list: A list of dictionaries where each dictionary contains the category and the overhead amount.
    """
    overheads = []
    
    # Open the CSV file and create a dictionary reader
    with open(file_path, 'r', encoding='utf-8-sig') as file:  # Use encoding to handle BOM
        reader = csv.DictReader(file)
        
        # Loop over each row in the CSV file
        for row in reader:
            # Store the category and overhead in a dictionary
            category = row['Category']
            overhead = float(row['Overheads'])
            overheads.append({'category': category, 'overhead': overhead})
    
    return overheads

def find_highest_overhead(overheads):
    """
    Finds the category with the highest overhead.
    
    Parameters:
    overheads (list): A list of dictionaries containing the category and overhead amount.

    Returns:
    dict: A dictionary containing the category and the highest overhead amount.
    """
    highest_overhead = {'category': '', 'overhead': 0}
    
    # Loop over each category's overhead to find the highest
    for category_data in overheads:
        if category_data['overhead'] > highest_overhead['overhead']:
            highest_overhead = category_data
    
    return highest_overhead

# Example usage:
# overheads_data = read_overheads('Overheads.csv')
# highest_overhead = find_highest_overhead(overheads_data)
# print(f"Highest overhead category is {highest_overhead['category']} with an amount of {highest_overhead['overhead']}")

