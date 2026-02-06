def multiply_by_ten():
    print("Enter the letter 'q' at anytime to quit.")

    while True:
        number = input("\nEnter a number: ")
        if number.lower() == "q":
            break
        try:
            multiplied_number = int(number) * 10
        except ValueError:
            print(f"Not a valid number. Please try again.")
        else:
            print(multiplied_number)

multiply_by_ten()