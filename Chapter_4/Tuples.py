print("")
print("Defining a Tuple")

print("Parentheses make the tuple contents immutable")
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
print("")

# Parentheses make the tuple contents immutable.
# dimensions = (200, 50)
# Below line returns an error because it's trying to change the tuple.
# dimensions[0] = 250
# print(dimensions[0])
# print(dimensions[1])
# print("")

print("Looping Through All Values in a Tuple")
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)
print("")

print("Writing over a Tuple: Reassigning a Variable")
print("Original dimensions:")
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

print("\nModified dimensions:")
dimensions = (400, 100)
for dimension in dimensions:
    print(dimension)
print("")


