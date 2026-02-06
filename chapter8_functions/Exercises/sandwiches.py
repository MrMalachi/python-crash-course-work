def sandwich_items(*items):
    print("\nSandwich items ordered:")
    for item in items:
        print(f"- {item}")
    print("Your sando is ready!")

sandwich_items("ham", "cheddar cheese")
sandwich_items("salami", "mozzarella")
sandwich_items("turkey", "banana peppers")


