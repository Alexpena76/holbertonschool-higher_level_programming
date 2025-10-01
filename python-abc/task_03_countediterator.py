#!/usr/bin/python3
"""Module that provides CountedIterator class"""


class CountedIterator:
    """Iterator that counts how many items have been iterated"""

    def __init__(self, iterable):
        """
        Initialize a CountedIterator

        Args:
            iterable: any iterable object (list, tuple, string, etc.)
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Get the next item and increment the counter

        Returns:
            The next item from the iterator

        Raises:
            StopIteration: when there are no more items
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """
        Get the current count of items iterated

        Returns:
            The number of items that have been iterated
        """
        return self.count
