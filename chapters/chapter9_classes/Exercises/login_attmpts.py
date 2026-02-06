class User:
    """Simulates the creation of a user-profile."""

    def __init__(self, first_name, last_name, username, email):
        """Initialize a user's attributes."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email.lower()
        self.login_attempts = 0

    def describe_user(self):
        """Prints a summary of the user's information."""
        print(f"\nUser Info:"
              f"\nFirst name - {self.first_name}"
              f"\nLast name - {self.last_name}"
              f"\nUsername - {self.username}"
              f"\nEmail - {self.email}")

    def greet_user(self):
        """Prints a personalized greeting to the user."""
        print(f"\nWelcome back {self.username}!")

    def increment_login_attempts(self):
        """Increments the value of 'login_attempts' by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the value of login_attempts to 0, when called."""
        self.login_attempts = 0

# Make an instance of the User class.
user3 = User(
    "kristan",
    "buotte",
    "kbuotte",
    "KirbyBuotte@yahoo.com",
)

# Call the method increment_login_attempts() several times on the instance.
user3.increment_login_attempts()
user3.increment_login_attempts()
user3.increment_login_attempts()

# Print the value of login_attempts to make sure it was incremented.
print(user3.login_attempts)

# Call the method reset_login_attempts() on the instance.
user3.reset_login_attempts()

# Print the new value of login_attempts to make sure it reset to zero.
print(user3.login_attempts)