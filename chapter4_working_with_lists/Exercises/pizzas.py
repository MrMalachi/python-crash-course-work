pizzas = ["neapolitan", "new york style", "white", "margherita", "detroit style"]

for pizza in pizzas:
    print(f"My favorite pizzas are: {pizza.title()}")

friend_pizzas = pizzas[:]

friend_pizzas.append("chicago deep dish")

print("")

for pizza in friend_pizzas:
    print(f"My friend's favorite pizzas are: {pizza.title()}")


