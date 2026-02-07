from printing_functions import print_models, show_completed_models

unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

print_models(unprinted_designs[:], completed_models)

"""
# HOW TO MOVE ITEMS FROM A SEPARATE LIST WITHOUT USING FUNCTIONS
# Start with some designs that need to be printed.
unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed:")
for model in completed_models:
    print(model)
"""