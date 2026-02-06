all_orders = []

print("\nWelcome to WeebTea! Please select one of the options below:")

def make_boba_order(name, tea, sweetness_level, ice_level, topping):
    """Returns a dictionary that stores information about a persons order."""
    order_dictionary = {
        "Customer": name,
        "Tea Selection": tea,
        "Sugar Level": sweetness_level,
        "Ice Amount": ice_level,
        "Topping": topping,
    }
    return order_dictionary

while True:
    name = input("\nWhat is your name? ")
    tea = input(
        "\n--- TEA MENU ---\n1. Black Milk Tea\n2. Jasmine Milk Tea"
        "\n3. Red Thai Milk Tea\n4. Green Thai Milk Tea"
        "\nWhich tea would you like? (enter a number) "
    )
    sweetness_level = input(
        "\n--- SUGAR LEVEL ---\n1. 100%\n2. 75%\n3. 50%\n4. 25%\n5. 0%"
        "\nWhich sugar level would you like for your drink? (enter a number) "
    )
    ice_level = input(
        "\n--- ICE AMOUNT ---\n1. Regular Ice\n2. Light Ice\n3. No Ice"
        "\nHow much ice would you like in your drink? (enter a number) "
    )
    topping = input(
        "--- TOPPINGS ---\n1. Brown Sugar Boba\n2. Crystal Boba"
        "\n3. Coffee Jelly\n4. None"
        "\nWhich topping would you like to add to your drink? (enter a number) "
    )
    menu_choice = input(
        "\n--- MENU OPTIONS ---\n1. Order Again\n2. Finish\n"
    )

    order = make_boba_order(name, tea, sweetness_level, ice_level, topping)
    all_orders.append(order)

    if menu_choice == 2:
        break

print(all_orders)








