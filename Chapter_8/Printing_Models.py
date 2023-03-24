print("\nPassing a List")
print("Modifying a List in a Function")
print("Example that does not use any functions\n")

# Start with some designs that need to be printed & an empty list.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Display all completed models
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(f"\t{completed_model.title()}")


print("\n\nModifying a List in a Function")
print("Example that uses functions\n")

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design until none are left.
    Move each design to completed models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(f"\t{completed_model.title()}")

unprinted_designs = ['jump box', 'zodiac necklace', 'pentagon']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


print("\n\nPreventing a Function from Modifying a List")
print("Using the Slice Notation [:]\n")

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design until none are left.
    Move each design to completed models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(f"\t{completed_model.title()}")

unprinted_designs = ['jump box', 'zodiac necklace', 'pentagon']
completed_models = []

# By passing [:] into the function call, the list the original list remains unchanged.
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(f"\nIntact Unprinted Designs List: {unprinted_designs}")

print()