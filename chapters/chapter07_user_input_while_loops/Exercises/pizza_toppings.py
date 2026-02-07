# Assigning two strings to the variable 'prompt', which prompts the user to follow instructions
# prompt +=: prompt = prompt + "\n(Type 'quit' once you are finished to exit.) "
# prompt += was used because the line of code is too long for just one line
prompt = "\nEnter any pizza toppings you'd like to add to your pizza:"
prompt += "\n(Type 'quit' once you are finished to exit.) "

# Assigning the boolean value 'True' to the variable 'active' to create a flag
active = True

# while 'active' is True, the user's input will be received
while active:
    user_input = input(prompt).title()

    if user_input == "Quit":    # if the user's input is equal to "quit/Quit"
        active = False  # the flag will be raised & set to False
        print("\nThank you, your toppings have been added!")
        break   # break out of the while loop
    else:
        print(f"\n{user_input} will be added to your pizza.") # otherwise, do the following...