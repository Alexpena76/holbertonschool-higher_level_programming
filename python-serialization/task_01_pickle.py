#!/usr/bin/python3
"""
Module for custom object serialization using pickle
"""
import pickle


class CustomObject:
    """
    Custom class with serialization capabilities using pickle
    """

    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject

        Args:
            name: string representing the person's name
            age: integer representing the person's age
            is_student: boolean indicating if person is a student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes in a formatted way
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance to a file using pickle

        Args:
            filename: name of the file to save the serialized object

        Returns:
            None if an error occurs during serialization
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance from a file using pickle

        Args:
            filename: name of the file to load the serialized object from

        Returns:
            CustomObject instance if successful, None if file doesn't exist
            or is malformed
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError, Exception):
            return None
