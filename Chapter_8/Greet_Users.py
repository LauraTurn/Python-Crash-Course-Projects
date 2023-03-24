print("\nPassing a List\n")

def greet_users(names):
    """Print a simple greeting to each user in a list."""
    for name in names:
        message = f"Hello, {name.title()}!"
        print(message)

usernames = ['hannah', 'ty', 'margot']

greet_users(usernames)

print()