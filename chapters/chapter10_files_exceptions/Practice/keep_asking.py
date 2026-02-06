while True:
    try:
        whole_number = int(input("Enter a whole number: "))
    except ValueError:
        print("Invalid input. Try again.")
    else:
        number_squared = whole_number ** 2  # Value must be stored in a var.
        print(number_squared)
        break


