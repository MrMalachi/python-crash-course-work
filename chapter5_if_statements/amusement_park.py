# Senior discount added to if-elif-else Chain
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")  # revised code is easier to modify: to change the text of the output message, you would need to change only one print() call rather than three separate print() calls

"""
# CONCISE if-elif-else Chain
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")  # revised code is easier to modify: to change the text of the output message, you would need to change only one print() call rather than three separate print() calls
"""

"""
# if-elif-else Chain
age = 12
if age < 4:
    print("Your admission cost is $0.") # the if test block evaluates to False, so its code is skipped
elif age < 18:
    print("Your admission cost is $25.")    # the elif test block evaluates to True, so its code is executed...
else:
    print("Your admission cost is $40.")    # ...and therefore, the else test block is skipped since the elif test block was executed
"""

