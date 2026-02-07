# This program creates a list containing Boba Tea items & then uses all functions/methods introduced in ch. 3
milk_tea_list = ["black milk tea", "jasmine milk tea", "oolong milk tea", "royal milk tea", "green thai milk tea", "red thai milk tea"]

# .append() method
milk_tea_list.append("strawberry milk tea")

# .insert() method
milk_tea_list.insert(0, "blue butterfly pea flower milk tea")

# .pop() method to remove the last item in the list
popped_milk_tea = milk_tea_list.pop()

# .remove() method to permanently remove red thai milke tea from the milk tea list
milk_tea_list.remove("red thai milk tea")

# .sort() method to permanently sort the items in the list alphabetically
milk_tea_list.sort()

# .sorted() function to temporarily sort items in the list reverse-alphabetical order
print(sorted(milk_tea_list, reverse=True))

# .reverse() method to permanently change the order of the milk tea list back to how it was originally
milk_tea_list.reverse()

# len() function to find the length of the list
print(f"There are currently {len(milk_tea_list)} items on the menu.")

print(milk_tea_list[6])

