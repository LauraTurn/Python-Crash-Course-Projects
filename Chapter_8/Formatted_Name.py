print("\nReturn Values")
print("Returning a Simple Value\n")

def get_formatted_name(first_name, last_name):
    """Return full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)


print("\n\nMaking an Argument Optional\n")

def get_formatted_name(first_name, middle_name, last_name):
    """Return full name, neatly formatted"""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)


print("\n\nMaking an Argument Optional Part 2\n")

def get_formatted_name(first_name, last_name, middle_name='', ):
    """Return full name, neatly formatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}" 
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)