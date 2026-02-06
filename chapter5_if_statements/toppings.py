# Using multiple lists
# What if a customer actually wants french fries on their pizza?
available_toppings = ["mushrooms", "olives", "green peppers", "pepperoni", "pineapple", "extra cheese"]

requested_toppings = ["mushrooms", "french fries", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")

"""
# Check that a list is NOT empty
requested_toppings = []

if requested_toppings:  # when the name of a list is used in an if-statement, Python returns True if the list contains at least one item;
    for requested_topping in requested_toppings:    # an empty list evaluates to False
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

"""

"""
# Using a for-loop to announce each topping as it's added to the pizza for efficiency
# Using an if-statement if the pizzeria runs out of green peppers
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print(f"Sorry, we are out of {requested_toppings[1]} right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")
"""

"""
# Testing Multiple Conditions
requested_topping = ["mushrooms", "extra cheese"]

if "mushrooms" in requested_topping:
    print("Adding mushrooms.")
if "pepperoni" in requested_topping:
    print("Adding pepperoni.")
if "extra cheese" in requested_topping:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
"""

"""
requested_topping = "mushrooms"

if requested_topping != "anchovies":
    print("Hold the anchovies!")
"""