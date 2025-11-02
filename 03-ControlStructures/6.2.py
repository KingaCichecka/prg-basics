###
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#
light_switch1 = True  # False = switch off, True = switch on
light_switch2 = False
bulbs_on = 0

if light_switch1:
    bulbs_on += 1   # switch 1 controls 1 bulb
if light_switch2:
    bulbs_on += 2   # switch 2 controls 2 bulbs

print(f"Number of bulbs on: {bulbs_on}")
