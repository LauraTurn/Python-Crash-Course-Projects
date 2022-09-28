print("")
print("Working with Part of a List: Slicing a List")

print("Print the first 3 items in a list:")
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print("")

print("Print the 2nd, 3rd & 4th items in a list:")
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])
print("")

print("If the first index is missing, Python starts with the first item:")
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])
print("")

print("If the last index is missing, Python runs through the end of the list:")
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])
print("")

print("Negative integers output the last items on a list:")
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])
print("")
print("")

print("Looping Through a Slice")
print("Here are the first three players on my team:")
players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players[:3]:
    print((player.title()))
print("")

print("Copying a List")
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

# This doesn't work:
# friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("")
print("")
