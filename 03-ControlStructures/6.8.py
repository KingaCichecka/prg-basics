###
# Checks if the entered name is a Polish female name
#
name = input("Enter name: ")

if name.endswith("a"):
    print(f"{name} — Polish female name")
else:
    print(f"{name} — not a Polish female name")
