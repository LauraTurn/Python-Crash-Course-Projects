print("\nChecking for Inequality")

requested_topping = 'mushroom'
if requested_topping != 'anchovies':
    print("Hold the anchovies!\n")

requested_topping = 'anchovies'
if requested_topping != 'anchovies':
    print("Hold everything else!")
# No expected output

print("Checking Whether a Value is in a List")
# Code Check
# requested_toppings = ['mushrooms', 'onion', 'pineapple']
# 'mushrooms' in requested_toppings
# True
# 'pepperoni' in requested_toppings
# False


print("\nTesting Multiple Conditions")
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("Finished making your pizza!")


print("\nChecking for Special Items")
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("Finished making your pizza!\n")

toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_toppings in toppings:
    print(f"Adding {requested_toppings}.")
print("Finished making your pizza!\n")

toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_toppings in toppings:
    if requested_toppings == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_toppings}.")
print("Finished making your pizza!")


print("\nChecking that a List is not Empty")
toppings = []
if requested_toppings in toppings:
    for requested_toppings in toppings:
        print(f"Adding {requested_toppings}.")
    print("Finished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")


print("\nUsing Multiple Lists")
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping} to add to your pizza.")
print("Finished making your pizza!\n")
