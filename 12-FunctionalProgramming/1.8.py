initials = lambda name, surname: name[0].upper() + surname[0].upper()

name = input("Enter name: ")
surname = input("Enter surname: ")

print("Initials:", initials(name, surname))
