print("Enter two numbers and I'll add them together. ")
print("Enter 'q' to quit.")

# Use a while loop to continuously ask for input, until the user enters 'q'.
while True:
    number1 = input("First number: ")
    if number1 == "q":
        break
    number2 = input("Second number: ")
    if number2 == "q":
        break

    try:
        # Convert both strings to integers and assign to variable 'answer'.
        answer = int(number1) + int(number2)
    except ValueError:  # Catches exception object in case of string input.
        # Print a user-friendly error message.
        print("You can't add letters! Please try again.")
    else:
        print(answer)   # Print the user's added numbers otherwise.







