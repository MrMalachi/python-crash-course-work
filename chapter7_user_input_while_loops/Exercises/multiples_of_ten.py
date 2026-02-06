number = input("Please enter a number: ")
number = int(number)

if number % 10 == 0:
    print(f"{number} IS a multiple of 10.")
else:
    print(f"{number} IS NOT a multiple of 10.")