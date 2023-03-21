print("\nUsing Break to Exit a Loop\n")

prompt = "\nPLease enter the name of a city you have visited:"
prompt += "\n\t(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"\nI'd love to go to {city.title()}!")

print()