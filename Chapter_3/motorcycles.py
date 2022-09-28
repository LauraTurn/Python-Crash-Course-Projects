print("\nSets a list of items")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(f"1.{motorcycles}\n")

print("Replaces the first item in the list")
motorcycles[0] = 'ducati'
print(f"2. {motorcycles}\n")

print("Adds ducati to the end of the list")
motorcycles.append('ducati')
print(f"3. {motorcycles}\n")

print("Starts with an empty list of items and adds them one by one")
motorcycle = []
print(f"4a. {motorcycle}")

motorcycle.append('honda')
motorcycle.append('yamaha')
motorcycle.append('suzuki')
print(f"4b. {motorcycle}\n")

print("Sets a list of items and inserts one at the beginning")
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(f"5. {motorcycles}\n")

print("Sets a list of items and deletes the first")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(f"6a. {motorcycles}")
del motorcycles[0]
print(f"6b. {motorcycles}\n")

print("Sets a list of items and deletes the second")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(f"7a. {motorcycles}")
del motorcycles[1]
print(f"7b. {motorcycles}\n")

print("Pops an item from a list")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(f"8a. {motorcycles}")
popped_motorcycle = motorcycles.pop()
print(f"8b. {motorcycles}")
print(f"8c. {popped_motorcycle}\n")

print("Context for popping an item from a list")
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"9. The last motorcycle I owned was a {last_owned.title()}.\n")

print("Popping an item by position from a list")
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"10. The first motorcycle I owned was a {first_owned.title()}.\n")

print("Removing an item by value")
motorcycles = ['honda', 'yamaha', 'ducati', 'suzuki']
print(f"11a. {motorcycles}")
motorcycles.remove('ducati')
print(f"11b. {motorcycles}\n")


print("Context for removing an item by value")
motorcycles = ['honda', 'yamaha', 'ducati', 'suzuki']
print(f"12a. {motorcycles}")
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(f"12b. A {too_expensive.title()} is too expensive for me!")
