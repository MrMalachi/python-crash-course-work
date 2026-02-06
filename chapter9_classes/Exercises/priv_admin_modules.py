"""This is a module containing both the Privileges and Admin class."""
from privileges import User

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



