def get_initials(name, uppercase=True):
    if not uppercase:
        return name[0]
    return name[0].upper()

first_name = input("Enter your first name: ")
first_name_initial = get_initials(name=first_name)
print('Your initials are: ' + first_name_initial)