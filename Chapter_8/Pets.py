print("\nPassing Arguments")
print("Positional Arguments")
print("\nPostional arguments need to be in the same order the parameters were written.")

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')


print("\n\nMultiple Function Calls")
print("Remember, order matters in positional arguments.")

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')


print("\n\nKeyword Arguments")
print("A keyword argument is a name-value pair that you pass to a function.")

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')


print("\n\nDefault Value")
print("Used if a parameter is not provided in the function call, positional.")

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='harriet', animal_type='hamster')
describe_pet(pet_name='snackers')


print("\n\nKeyword Arguments")
print("A keyword argument is a name-value pair that you pass to a function.")

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')


print("\n\nEquivalent Function Calls")
print("Used if a parameter is not provided in the function call, positional.")

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# A dog name Frisky
describe_pet('frisky')
describe_pet(pet_name='frisky')

# A mare named Mittens
describe_pet('mittens', 'mare')
describe_pet(animal_type='mare', pet_name='mittens')
describe_pet(pet_name='mittens', animal_type='mare')