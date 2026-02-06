def make_sandwich(*ingredients):
    """Print a list of ingredients using positional arguments."""
    print("\nSandwich Ingredients:")

    # Iterate through the ingredients provided.
    for ingredient in ingredients:
        print(f"- {ingredient.title()}")

make_sandwich("ham", "sharp cheddar")
make_sandwich("steak", "chipotle mayo", "provolone", "peppers")
make_sandwich("cheddar cheese")





