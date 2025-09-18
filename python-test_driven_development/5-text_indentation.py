#!/usr/bin/python3
"""
This module provides a function to format text with proper indentation.
It handles text processing by adding double newlines after specific characters.
The function ensures proper spacing and removes leading/trailing spaces.
Validates that the input is a string before processing.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?', and ':' characters.
    Removes spaces at the beginning and end of each line.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    i = 0
    while i < len(text):
        char = text[i]
        print(char, end="")
        
        if char in '.?:':
            print("\n")
            i += 1
            # Skip any spaces that follow the special character
            while i < len(text) and text[i] == ' ':
                i += 1
        else:
            i += 1
