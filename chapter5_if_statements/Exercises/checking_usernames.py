# This program determines whether or not a username is already being used

# List of current usernames
current_users = ["GoldenBoy", "BrownBEAST4", "coolacola", "elitooicy", "malachi__brown"]
# List of new usernames
new_users = ["GoldenBoy", "CoolaCola", "michah._.brown", "hezo_melo", "noirblanco"]

# Making a copy of the variable 'current_users' containing the lowercase versions of all existing users
current_users_lower = [username.lower() for username in current_users]

# Iterating through the 'new_users' list to check if newly created usernames pre-exist in the 'current_users' list
for username in new_users:
    if username.lower() in current_users_lower:
        print(f"Sorry, the username '{username}' is already being used.")
    else:
        print(f"The username '{username}' is available to use.")
