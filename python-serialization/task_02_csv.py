#!/usr/bin/env python3
"""
Module to convert CSV files to JSON format.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to JSON format and write to data.json.
    
    Args:
        csv_filename (str): The name of the CSV file to convert
        
    Returns:
        bool: True if conversion was successful, False otherwise
    """
    try:
        # List to store all rows as dictionaries
        data = []
        
        # Open and read the CSV file
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            # Use DictReader to convert each row into a dictionary
            csv_reader = csv.DictReader(csv_file)
            
            # Add each row to the data list
            for row in csv_reader:
                data.append(row)
        
        # Write the JSON data to data.json
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        
        # Return True if successful
        return True
        
    except FileNotFoundError:
        # Handle file not found error
        print(f"Error: The file '{csv_filename}' was not found.")
        return False
    
    except Exception as e:
        # Handle any other exceptions
        print(f"Error: An unexpected error occurred: {e}")
        return False