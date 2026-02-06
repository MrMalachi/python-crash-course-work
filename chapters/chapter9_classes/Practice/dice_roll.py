from random import randint

class Die:
    """
    Simulates a board game requiring rolling two dice until both show the same number.
    """

    def __init__(self, sides=6):
        """Initialize attributes."""
        self.sides = sides
        self.counter = 0

    def roll(self):
        """Returns a random number until both die match."""
        return randint(1, self.sides)

# Create instance from the Die class
die1 = Die()
die2 = Die()

roll_count = 0

while True:
    roll_count += 1

    roll_1 = die1.roll()
    roll_2 = die2.roll()

    if roll_1 == roll_2:
        break

print(f"It took {roll_count} rolls until both dice matched.")
