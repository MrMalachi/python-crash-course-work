# Create a list of customer sandwich orders.
sandwich_orders = ["cuban", "pastrami", "bánh mì", "reuben", "pastrami", "club",
                   "grilled cheese", "cheesesteak", "pastrami"]
# Create an empty list that will hold completed sandwiches.
finished_sandwiches = []

# NO MORE PASTRAMI!
print("\nSorry, but Malachi's Deli has run out of Pastrami for the day.\n")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

# While the list 'sandwich_orders' evaluates to True,
# (while there are still values contained in the list), use the .pop() method.
while sandwich_orders:
    sandwich_made = sandwich_orders.pop()   # Temporarily removes & then stores
                                            # values into the variable 'sandwich_made'.
    # Display the message for each sandwich that has been prepared.
    print(f"I'm working on your {sandwich_made.title()} sandwich.")
    # Add the sandwiches from 'sandwiche_made' variable to the empty list 'finished_sandwiches'.
    finished_sandwiches.append(sandwich_made)

print("\nFinished sandwiches:")

# Display every sandwich in the list of 'finished_sandwiches'
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()}")




