from random import choice

class PasswordGenerator:
    """Simulates a system generating temporary access codes."""

    # Create class attribute because it will not change.
    password_tuple = (
        "z", "y", "x", "w", "v", "u", "t", "s",
        "8", "7", "6", "5", "4", "3", "2", "1",
        "@", "#", "$", "%", "!", "?",
    )

    def __init__(self):
        """Initialize attributes."""
        self.access_code = []
        self.counter = 0

    def generate_code(self):
        """Generates a random 4-digit access code."""
        # 'random_combo' list used in method to refresh the list every call.
        self.access_code = []

        # Use a for-loop to iterate 4x through the password_tuple (immutable).
        for _ in range(4):
            random_combo = choice(self.password_tuple)
            self.access_code.append(random_combo)

password = PasswordGenerator()

password.generate_code()

# Use the asterisk operator to unpack the list for a neater format.
print(f"Temporary Access Code:")
print(*password.access_code)





