#!/usr/bin/python3
"""Module that demonstrates multiple inheritance with FlyingFish"""


class Fish:
    """Fish class with swim and habitat methods"""

    def swim(self):
        """Fish swimming behavior"""
        print("The fish is swimming")

    def habitat(self):
        """Fish habitat"""
        print("The fish lives in water")


class Bird:
    """Bird class with fly and habitat methods"""

    def fly(self):
        """Bird flying behavior"""
        print("The bird is flying")

    def habitat(self):
        """Bird habitat"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish class that inherits from both Fish and Bird"""

    def swim(self):
        """Override swim method"""
        print("The flying fish is swimming!")

    def fly(self):
        """Override fly method"""
        print("The flying fish is soaring!")

    def habitat(self):
        """Override habitat method"""
        print("The flying fish lives both in water and the sky!")
