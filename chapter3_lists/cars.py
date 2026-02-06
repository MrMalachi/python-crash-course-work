cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()

print(cars)

cars = ["bmw", "audi", "toyota", "subaru"]
# This passes the argument reverse=True to sort the list in unalphabetical order
cars.sort(reverse=True)

print(cars)

# Using the sorted() Function to TEMPORARILY sort a list without affecting the actual order of the list
cars = ["bmw", "audi", "toyota", "subaru"]

print("\nHere is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# Using the .reverse() method to permanently chronologically sort the 'cars' list
print("\nHere is the original list again:")
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)

cars.reverse()
print(f"\nHere is the reversed list: \n{cars}")