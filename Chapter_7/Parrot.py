print("\nHow the Input() Function Works\n")

message = input("Tell me something, and I will repeat it back to you: ")
print(f"\n\"{message}\"")

print()


print("\nLetting the User Choose When to Quit")

prompt = "\nTell me something and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. You say: "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(f"\nParrot says: {message}")
    else:
        print("\n\tThanks for playing with the parrot!")
        
print()


print("\nUsing a Flag")

prompt = "\nTell me something and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program. You say: "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
         active = False
    else:
        print(f"\nParrot says: {message}")
print("\n\tThanks for playing with the parrot!")

print()
