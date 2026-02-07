"""Import the choice function from the random module in Python Standard Lib."""
from random import choice

class Lottery:
    """Simulates a lottery."""

    lottery = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e")

    def __init__(self):
        """Initialize attributes."""
        self.winning_sequence = []
        self.my_ticket = []
        self.counter = 0

    def read_rules(self):
        """Display the lottery rules."""
        print(f"\nWelcome to 111 Lottery. "
              f"The jackpot lucky winner cash prize is $1,111,111!"
              f"\nMatch the following winning numbers/letters to win: ", end="")

    def generate_lottery(self):
        """Simulates the lucky numbers/letters for players."""
        for _ in range(4):
            drawing = choice(self.lottery)
            self.winning_sequence.append(drawing)

        print(self.winning_sequence)

    def draw_ticket(self):
        """Draw a ticket for oneself UNTIL it matches the 'winning_sequence'."""
        while True:
            # Reset ticket each round
            self.my_ticket = []

            for _ in range(4):
                ticket_drawing = choice(self.lottery)
                self.my_ticket.append(ticket_drawing)

            print(self.my_ticket)
            self.counter += 1

            if self.my_ticket == self.winning_sequence:
                print("You won!")
                break

    def display_loop_report(self):
        """
        Prints the amount of times it took
        for the person to draw a winning ticket.
        """
        print(f"It took you {self.counter} tries to win!")

gambler = Lottery()

gambler.read_rules()
gambler.generate_lottery()
gambler.draw_ticket()
gambler.display_loop_report()
