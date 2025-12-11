avg_speed = lambda distance, hours, minutes: distance / (hours + minutes / 60)

distance = float(input("Enter distance in km: "))
hours = int(input("Enter number of travel hours: "))
minutes = int(input("Enter number of travel minutes: "))

result = avg_speed(distance, hours, minutes)
print(f"Average speed: {result:.1f} km/h")
