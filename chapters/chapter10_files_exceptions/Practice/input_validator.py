def product_cal(number1, number2):
    """Returns the product of two numbers."""
    return number1 * number2

while True:
        number1 = input("\nEnter your first number (or 'q' to quit): ")
        if number1 == "q":
            break
        number2 = input("Enter your second number (or 'q' to quit): ")
        if number2 == "q":
            break

        try:
            num1 = int(number1)
            num2 = int(number2)
        except ValueError:
            print(f"You must enter a whole number! Please try again...")
        else:
            product = product_cal(num1, num2)
            print(f"{num1} * {num2} = {product}")
