# Prompt the user to enter their age
prompt = input("\nTo purchase a movie ticket, please enter your age: ")

# Explicit type conversion from string to integer
# Assign the prompt variable (which is the user's input) to the age variable
age = int(prompt)

# Conditional if-elif-else chain to determine the price of the user's movie ticket
# This of course, is dependent on the user's age (the age they enter)
if age < 3:
    print("Your movie ticket price is free.99.")
elif age < 12:
    print("Your movies ticket price is $10")
else:
    print("Your movie ticket price is $15")