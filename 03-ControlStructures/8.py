###
# Sums numbers entered by user and calculates their arithmetic mean
#
total_sum = 0
count = 0   # licznik wprowadzonych liczb

while True:
    number = int(input("Enter a number (0 to stop): "))

    if number == 0:
        break   # zakończ, jeśli wpisano 0

    total_sum += number
    count += 1  # zwiększ licznik o 1

# Obliczenie średniej tylko, jeśli podano jakieś liczby
if count > 0:
    average = total_sum / count
    print(f"The total sum of the numbers is: {total_sum}")
    print(f"The arithmetic mean of the numbers is: {average}")
else:
    print("No numbers were entered.")