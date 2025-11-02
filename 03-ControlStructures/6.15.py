###
# Washing machine total time calculator
#
# Programs: jacket=40 min, underwear=70 min, shoes=20 min
# Extras: rinse=15 min, spin=9 min
total_washing_time = 0

program = input("Select washing program: (j)acket, (u)nderwear, (s)hoes: ").lower()
extra_rinse = input("Extra rinse? (y/n) ").lower()
extra_spin  = input("Extra spin? (y/n) ").lower()

if program == 'j':
    total_washing_time += 40
elif program == 'u':
    total_washing_time += 70
elif program == 's':
    total_washing_time += 20
else:
    print("Unknown program!")

if extra_rinse == 'y':
    total_washing_time += 15
if extra_spin == 'y':
    total_washing_time += 9

print(f"Total washing time: {total_washing_time} minutes")
