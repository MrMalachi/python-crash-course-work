unprinted_models = ["car", "robot", "headphones"]
completed_models = []

def print_models(unprinted_models, completed_models):
    """Simulate printing each 3D-model, until none are left."""
    print("Building 3-D Models:")

    # Runs as long as 'unprinted_models' list is not empty
    # *Remember*, an empty list=False, and a list with items=True
    while unprinted_models:
        current_model = unprinted_models.pop()
        print(f"Scanning {current_model}...")
        completed_models.append(current_model)

def show_completed_models(completed_models):
    """Display the completed 3-D models printed."""
    print("\nCompleted 3-D Models:")

    for model in completed_models:
        print(model)

print_models(unprinted_models, completed_models)
show_completed_models(completed_models)










