print("\nReturning a Dictionary\n")

def build_person(first_name, last_name):
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jim', 'hendrix')
print(musician)


print("\n\nReturning a Dictionary with Optional Values\n")

def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jim', 'hendrix', age=27)
print(musician)

musician = build_person('john', 'hooker')
print(musician)