def avg_speed(distance, hours, minutes):
    time = hours + minutes / 60
    return distance / time

distance = float(input("Enter distance in km: "))
hours = int(input("Enter number of travel hours: "))
minutes = int(input("Enter number of travel minutes: "))

speed = avg_speed(distance, hours, minutes)
print(f"Average speed: {speed:.1f} km/h")