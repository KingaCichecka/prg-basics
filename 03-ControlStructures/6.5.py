###
# Parking meter - calculates fee based on hours
#
hours = int(input("Enter the number of hours parked: "))

if hours <= 2:
    fee = 5
elif hours <= 6:
    fee = 15
else:
    fee = 20

print(f"The parking fee is {fee} PLN.")
