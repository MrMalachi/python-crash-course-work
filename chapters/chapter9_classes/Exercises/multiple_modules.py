"""Utilizes the priv_admin module to import classes."""

from priv_admin_modules import Admin, Privileges

# Create an administrator instance and assign it to admin2.
admin2 = Admin(
    "daniel",
    "boakye",
    "GhanianL0rd",
    "dan_dan_dan@yahoo.com"
)

# self.privileges = Privileges() in the initializer method of the Admin class
# allows you to access the empty list through the attribute and add strings.
admin2.privileges.privileges_list = [
    "can ban users",
    "can put users in timeout",
    "can moderate livestreams"
]

# Call the method through the privileges attribute on the object.
admin2.privileges.show_privileges()

