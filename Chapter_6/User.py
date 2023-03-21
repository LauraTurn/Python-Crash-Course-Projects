print("\nLooping Through a Dictionary")

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

print("\nLooping Through All the Keys in a Dictionary\n")

for data_type in user_0.keys():
    print(data_type.title())

print()

#Displays the same information even when omitting .keys()
#.keys() is the default behavior of a loop
for data_type in user_0:
    print(data_type.title())