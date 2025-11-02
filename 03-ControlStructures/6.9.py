###
# Calculates dog's age in dog's years
#
age_human = float(input("Enter the dog's age in human years: "))

if age_human <= 2:
    age_dog = age_human * 10.5
else:
    age_dog = 21 + (age_human - 2) * 4

print(f"The dog's age in dog's years is {age_dog} years.")
