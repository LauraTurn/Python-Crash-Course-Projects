# Permanently sort list alphabetically
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(f"\n{cars}")

# Permanently sort list of car in reverse order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(f"{cars}\n")

# Temporarily sort a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"Here is the original list: {cars}")
print(f"Here is the sorted list: {sorted(cars)}")
print(f"Here is the original list again: {cars}\n")

# Printing a List in Reverse Order (strictly reverse order)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"{cars}")
cars.reverse()
print(f"{cars}\n")

# Finding the length of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"{len(cars)}\n")
