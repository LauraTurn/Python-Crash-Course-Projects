print("\nIntroducing while Loops")

print("\nThe While Loop in Action\n")

# Loops through a series of numbers

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
print()


print("\nUsing Continue in a Loop\n")

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

print()


print("\nAvoiding Infinite Loops\n")

# Omitting 'x += 1' will create a loop that runs forever
x = 1
while x <= 5:
    print(x)
    x += 1

print()
