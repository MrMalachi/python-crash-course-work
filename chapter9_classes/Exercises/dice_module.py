"""
A module containing the imported module from the Python Standard Library and
the 'Die' class.
"""

from random import randint

class Die:
    """A class simulating a single die roll."""

    def __init__(self, sides=6):
        """Initialize attributes."""
        self.sides = sides

    def roll_die(self):
        """Returns a random number between 1 and number of sides the die has."""
        number_rolled = randint(1, self.sides)
        return number_rolled    # Return the result for later use.




