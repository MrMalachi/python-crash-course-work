from random import choice

class Elevator:
    """Simulates an elevator."""

    floor_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

    def __init__(self):
        """Initialize attributes."""
        self.counter = 0

    def stop_at_floor(self):
        """Randomly stop at a floor."""
        while True:
            self.counter += 1

            floor = choice(self.floor_numbers)
            if floor != 1:
                print("Elevator is still moving...")
            else:
                print("Stopping at floor 1...")
                break

elevator = Elevator()

elevator.stop_at_floor()

if elevator.counter == 1:
    print(f"It took {elevator.counter} stop to reach floor 1.")
else:
    print(f"It took {elevator.counter} stops to reach floor 1.")