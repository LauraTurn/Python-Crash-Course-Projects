print("\nStoring Your Function in Modules")

# Module: a file ending in .py that contains cod you want to import into your program.
# Imported to making_pizzas.py & making_pizzas2.py

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
