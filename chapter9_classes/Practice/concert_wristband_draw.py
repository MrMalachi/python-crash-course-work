from random import choice

class WristbandDraw:
    """Simulate a winning wristband code at a concert."""

    lottery_draw = (1, 2, 3, 4, 5, 6, 7, 8, "a", "b", "c", "d", "e", "f", "g")

    def __init__(self):
        """Initialize attributes."""
        self.winning_sequence = []
        self.my_wristband = []
        self.counter = 0

    def generate_winning_code(self):
        """Randomly select 3 items to create a winning wristband code."""
        # Create an empty list to store the winning code in.
        self.winning_sequence = []

        for _ in range(3):
            code = choice(self.lottery_draw)
            self.winning_sequence.append(code)

    def display_winning_code(self):
        """Print the winning wristband code sequence."""
        print(f"Winning Code: {self.winning_sequence}")

    def generate_my_code(self):
        """Check if my_wristband matches the winning code."""
        # Create a variable with 3 fixed values.
        self.my_wristband = ["a", 1, "e"]

        self.counter = 0

        while True:
            self.counter += 1

            self.generate_winning_code()

            if self.my_wristband == self.winning_sequence:
                print(f"Winner! It took you {self.counter} tries.")
                print(f"My Wristband: {self.my_wristband}")
                print(f"Winning Code: {self.winning_sequence}")
                break

# Create an instance from the WristbandDraw class
contestant = WristbandDraw()

contestant.generate_winning_code()
contestant.display_winning_code()

contestant.generate_my_code()




