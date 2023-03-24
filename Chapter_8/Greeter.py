print("\nDefining a Function\n")

def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()


print("\n\nPassing Information to a Function\n")

def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')


print("\n\nAguments and Paramters\n")

print("Parameter: A piece of information the function needs to do its job.")
print("\tFor example, 'username'\n")

print("Argument: A piece of information that's passed from a function call to a function.")
print("\tFor example, 'jesse'")


print("\n\nUsing a Function with a While Loop")

def get_formatted_name(first_name, last_name):
    """Return full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an infinite loop!
# while True:
#     print("\nPlease tell me your name.")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")

#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")

while True:
     print("\nPlease tell me your name.")
     print("Enter 'q' at any time to quit.")
     f_name = input("First name: ")
     if f_name == 'q':
         break
     l_name = input("Last name: ")
     if l_name == 'q':
         break

     formatted_name = get_formatted_name(f_name, l_name)
     print(f"\nHello, {formatted_name}!")

print()
print("Goodbye!")
print()
