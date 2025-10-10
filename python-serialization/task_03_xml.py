#!/usr/bin/env python3
"""
Module to serialize and deserialize data using XML format.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML format and save to a file.
    
    Args:
        dictionary (dict): The dictionary to serialize
        filename (str): The name of the XML file to create
    """
    # Create the root element
    root = ET.Element('data')
    
    # Iterate through dictionary items and add them as child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    
    # Create an ElementTree object and write to file
    tree = ET.ElementTree(root)
    
    # Write with proper formatting (indentation)
    ET.indent(tree, space="    ")
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file back into a Python dictionary.
    
    Args:
        filename (str): The name of the XML file to read
        
    Returns:
        dict: The deserialized dictionary
    """
    # Parse the XML file
    tree = ET.parse(filename)
    root = tree.getroot()
    
    # Reconstruct the dictionary
    dictionary = {}
    
    # Iterate through all child elements
    for child in root:
        # Add each element to the dictionary
        # The tag becomes the key, the text becomes the value
        dictionary[child.tag] = child.text
    
    return dictionary