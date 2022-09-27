print("")
print("Loop numbers 1-4")
for value in range(1, 5):
    print(value)
print("")

print("Loop numbers 1-5")
for value in range(1, 6):
    print(value)
print("")

# Lists even numbers by increments of 2
print("Loop to list even numbers 1-10")
even_numbers = list(range(2, 11, 2))
print(even_numbers)
print("")

print("Loop to list squared value of ints from 1-10")
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)
print("")

print("Loop to list squared value of ints from 1-10 concisely")
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)
print("")

print("Simple statistics with a list of numbers")
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f"Min number: {min(digits)}")
print(f"Max number: {max(digits)}")
print(f"Sum of all: {sum(digits)}")
print("")

print("Loop to list squared value of ints from 1-10 with list comprehension")
squares = [value**2 for value in range(1, 11)]
print(squares)
print("")
