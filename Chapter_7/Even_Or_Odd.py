print("\nThe Modulo Operator\n")

# The modulo operator(%): Divides one number by another and returns the remainder
# Does not tell you how many times just what the remainder is
# The below code can determine if a number is even or odd

number = input("Enter a number and I will tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
print()
