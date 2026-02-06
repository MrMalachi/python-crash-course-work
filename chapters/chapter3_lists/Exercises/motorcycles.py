"""
motorcycles = []

motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")

motorcycles.insert(0, "ducati")

del motorcycles[0]

print(motorcycles)

# motorcycles[0] = "ducati"

# motorcycles.append("ducati")
"""

"""
# Using the .pop() method to remove the last element from the list 'motorcycles' by creating a new variables called 'popped_motorcycle'
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)

print(popped_motorcycle)
"""

"""
# Defining a variable called 'last_owned' and assigning it to the motorcycles variable and attaching the .pop() method to it in order to use it in an f-string
motorcycles = ["honda", "yamaha", "suzuki"]

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")
"""

"""
# Popping Items from Any Position in a List
motorcycles = ["honda", "yamaha", "suzuki"]

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
"""

# Removing an Item by Value Because It's Too Expensive
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)

too_expensive = "ducati"
motorcycles.remove(too_expensive)

print(f"\nA {too_expensive.title()} is too expensive for me at the moment.")