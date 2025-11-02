###
# Determines user's age group
#
age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age <= 19:
    print("Teen")
elif age <= 64:
    print("Adult")
else:
    print("Senior")
