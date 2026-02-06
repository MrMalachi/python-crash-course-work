# Create a flag
active = True

# while the flag is "green" (True) do the following...
while active:
    prompt = input("\nEnter your age (or 'quit' to exit): ")    # prompt user

    # if input == "quit", the message will be printed & the program will end
    if prompt == "quit":
        print("Goodbye!")
        break   # ends program by breaking out of the while loop

    # convert the prompt variable's data type to integer & assign it to variable 'age'
    age = int(prompt)

    # One of the following conditions will be met IF it evaluates to True
    if age < 3:
        print("\nMovie Ticket Price: Free")
    elif age < 12:
        print("\nMovie Ticket Price: $10")
    else:
        print("\nMovie Ticket Price: $15")









