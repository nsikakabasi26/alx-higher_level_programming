#!/usr/bin/python3
"""
This module defines the MagicClass, a class for performing magical calculations.

The MagicClass can be used to calculate the area and circumference based on the provided radius.
"""

import math

class MagicClass:
    """
    A magical class for performing calculations on a radius.

    Attributes:
    __radius (float): The radius for magical calculations.
    """

    def __init__(self, radius):
        """
        Initialize the MagicClass with a given radius.

        Args:
        radius (float): The radius for magical calculations.

        Raises:
        TypeError: If the provided radius is not a valid number (int or float).
        """
        self.__radius = 0  # Default value

        # Check if radius is a valid number (int or float)
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        # Set the radius if it's a valid number
        self.__radius = radius

    def area(self):
        """
        Calculate and return the magical area based on the radius.

        Returns:
        float: The magical area.
        """
        return 2 ** self.__radius * math.pi

    def circumference(self):
        """
        Calculate and return the magical circumference based on the radius.

        Returns:
        float: The magical circumference.
        """
        return 2 * math.pi * self.__radius
