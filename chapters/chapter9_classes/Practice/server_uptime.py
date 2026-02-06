from random import choice

class CheckServerStatus:
    """Simulates a random uptime monitor for a server."""

    # A class attribute as a tuple containing server status.
    status = ("online", "online", "online", "offline")

    def __init__(self):
        """Initialize attributes."""
        self.check_count = 0

    def check_status(self):
        """Checks server status repeatedly until it goes 'offline'."""
        while True:
            self.check_count += 1   # Increment 'check_count' by 1

            # Use the choice function on the tuple and assign in to a variable.
            random_status = choice(self.status)
            if random_status == "offline":
                return random_status, self.check_count  # Return data

# Instantiation
status_level = CheckServerStatus()

# Assign the method call on the object to two variables
status, count = status_level.check_status()

# Display how many checks occurred.
if count == 1:
    print(f"Server went {status} after {count} check.")
else:
    print(f"Server went {status} after {count} checks.")


