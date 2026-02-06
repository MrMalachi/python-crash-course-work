"""This program utilizes the privileges module."""

from privileges import User, Privileges, Admin

# Create an instance from the imported Admin class.
admin1 = Admin(
    "nathaniel",
    "brown",
    "superprophet",
    "superprophet2002@outlook.com",
)

# Access the empty privileges list through the privileges attribute and fill it.
admin1.privileges.privileges_list = [
    "can suspend users",
    "can put users in timeout",
    "can reset username/password"
]

# Call the method through the privileges attribute on the object.
admin1.privileges.show_privileges()


