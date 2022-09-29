print("\nThe if-elif-else Chain")

age = 12
print(f"Your age is: {age}.")
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

# More efficient and easier to modify code.
age = 64
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"\nYour age is: {age}.")
print(f"Your admission cost is ${price}.")

# More efficient and easier to modify code.
print("\nUsing Multiple elif Blocks")
age = 18
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your age is: {age}.")
print(f"Your admission cost is ${price}.")

print("\nOmitting the else Block")
age = 67
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"Your age is: {age}.")
print(f"Your admission cost is ${price}.")

