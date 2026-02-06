from random import choice

class SmartLock:
    """
    Simulates a smart lock that unlocks only when a randomly generated code
    matches a target code.
    """

    # Create a class attribute that acts as a pool of random numbers/letters.
    code_pool = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e")

    def __init__(self):
        """Initialize attributes."""
        self.counter = 0

    def unlock_code(self):
        """Randomly select 4 items from 'code_pool' and store them in a list."""
        unlock_code = []

        for _ in range(4):
            random_code = choice(self.code_pool)
            unlock_code.append(random_code)

        return unlock_code

    def display_unlock_code(self):
        """Prints the unlock code."""
        print(f"Any code matching {self.unlock_code()} unlocks the door!")

    def attempt_to_unlock(self):
        """Represents the amount of attempt(s) it took to unlock door."""
        my_code = []

        while True:
            self.counter += 1

            for _ in range(4):
                attempt_code = choice(self.code_pool)
                my_code.append(attempt_code)

            if my_code == self.unlock_code():
                return self.counter



# Instantiation
attempt = SmartLock()

attempt.unlock_code()
attempt.display_unlock_code()
attempt.attempt_to_unlock()