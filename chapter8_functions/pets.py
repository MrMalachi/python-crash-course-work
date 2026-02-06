# The definition of 'describe_pet()' includes a default value,
# so now when the function is called with no animal_type specified,
# Python knows to use the value 'dog' for this parameter
def describe_pet(pet_name, animal_type="dog"):
    """Display information about pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name="rufus")

"""
pets.py -- KEYWORD ARGUMENTS

def describe_pet(animal_type, pet_name):
    """"""Display information about a pet.""""""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type="dog", pet_name="rufus")
# Notice here, the order of keyword arguments DOES NOT matter... Python knows
describe_pet(pet_name="harry", animal_type="hamster")
"""

"""
pets.py -- POSITIONAL ARGUMENTS

# The definition shows that this function needs a type of animal & the animal's name
def describe_pet(animal_type, pet_name):
    """"""Display information about a pet""""""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# When you call 'describe_pet', you need to provide an animal type and a name, in that order
describe_pet("hamster", "harry")
describe_pet("dog", "rufus")
"""