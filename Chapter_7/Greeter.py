print("\nWriting Clear Prompts\n")

name = input("Please enter your name: ")
print(f"\nHello, {name}!\n")

# Assigns the prompt to a variable and passesthat variable to the input() function
# Allows prompt to be built up so the imput statement is clean 
prompt = "\nIf you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!\n")


print("\nUsing Int() to Accept Numerical Input\n")
age = input("How old are you? ")

age = int(age)
print(age >= 18)

print()
