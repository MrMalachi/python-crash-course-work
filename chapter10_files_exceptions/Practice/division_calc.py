def get_numbers():
    """Prompt the user for two numbers and return them."""
    num1 = input("Enter your first number: ")
    num2 = input("Enter your second number: ")

    return num1, num2

def divide_numbers(num1, num2):
    """
    Divide first number by second number.
    Handles invalid input and division by zero.
    """
    try:
        divided_nums = int(num1) / int(num2)
    except ValueError:
        print("You must enter whole numbers. Please try again.")
    except ZeroDivisionError:
        print("You cannot divide by zero. Please try again.")
    else:
        print(divided_nums)

# Call the function & assign both values entered by the user to the variables.
num1, num2 = get_numbers()
# Call the function and pass both numbers entered by the user as arguments.
divide_numbers(num1, num2)


