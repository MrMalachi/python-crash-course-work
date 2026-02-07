def make_shirt(size="large", message="I love Python!"):
    """Display a sentence summarizing the t-shirt size & message printed."""
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f"It will say, '{message}'")

make_shirt()
make_shirt(size="medium")
make_shirt("small", "Programmer IQ")

