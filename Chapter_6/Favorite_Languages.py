print("\nA Dictionary of Similar Objects")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }

print(favorite_languages)

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")


print("\nLooping Through a Dictionary\n")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")


print("\nLooping Through All the Keys in a Dictionary\n")

for name in favorite_languages.keys():
    print(name.title())
print()    

friends = ['jen', 'sarah']
for name in favorite_languages:
    print(f"Hi {name.title()}")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
print()

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!\n")


print("\nLooping Through a Dictionary's Keys in a Particular Order\n")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, than you for taking the poll.")

print("\nLooping Through All Values in a Dictionary\n")

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
print()

#Set: A collection in which each item must be unique
#Sets do not retain items in any specific order
for language in set(favorite_languages.values()):
    print(language.title())
print()

languages = {'c', 'ruby', 'python', 'c#'}


print("\nA List in a Dictionary\n")

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
print()
