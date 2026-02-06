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

class Admin(User):
    """An administrator is a special kind of user, therefore, inherit 'User'."""

    def __init__(self, first_name, last_name, username, email):
        """Initialize the parent and child attributes."""
        super().__init__(first_name, last_name, username, email)
        self.privileges = Privileges()

class Privileges:
    """Simulates the privileges an admin can have."""

    def __init__(self):
        """Initialize the privilege class attributes."""
        self.privileges_list = []    # Default attribute (empty list).

    def show_privileges(self):
        """Lists the administrator's set of privileges."""
        print(f"\nAdministrator privileges:")
        for privilege in self.privileges_list:
            print(f"- {privilege}")


"""
admin1 = Admin(
    "malachi",
    "brown",
    "brownmn",
    "brown@gmail.com"
)

admin1.privileges.privileges_list = [
    "can add/delete posts",
    "can ban users",
    "can reset user passwords",
    "can change usernames upon request",
]

admin1.privileges.show_privileges()
"""