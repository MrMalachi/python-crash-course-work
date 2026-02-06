class User:
    """Simulates the creation of a user-profile."""

    def __init__(self, first_name, last_name, username, email):
        """Initialize a user's attributes."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email.lower()

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

# Create several instances representing different users.
user0 = User(
    "malachi",
    "brown",
    "brownBEAST4",
    "Brown@yahoo.com",
)

user1 = User(
    "david",
    "simmons",
    "DSgeneration",
    "dsimmons@yahoo.com"
)

user2 = User(
    "elisha",
    "brown",
    "elitooicy",
    "elisha@gmail.com"
)

# Call both methods for each instance.
user0.describe_user()
user0.greet_user()

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()
