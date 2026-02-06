"""
This program greets users in different manners and if there are no user's
in the list, a special message will appear.
"""

# List of usernames
usernames = ["admin", "BrownBEAST4", "Coolacola", "elitooicy", "malachi__brown"]

# Checks to make sure the list of usernames is NOT empty
if usernames:
    for username in usernames:  # for loop used to iterate over the list
        if username == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users!")    # special message if the list IS empty