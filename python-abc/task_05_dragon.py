#!/usr/bin/python3
"""Module that demonstrates mixin classes with Dragon"""


class SwimMixin:
    """Mixin that provides swimming capability"""

    def swim(self):
        """Swimming behavior"""
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides flying capability"""

    def fly(self):
        """Flying behavior"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that inherits from both SwimMixin and FlyMixin"""

    def roar(self):
        """Dragon's unique roaring behavior"""
        print("The dragon roars!")
