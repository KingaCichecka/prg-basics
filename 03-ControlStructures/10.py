###
# Takes a number from the user and counts down to zero.
# The last five seconds are displayed in words.
#
import time

countdown = int(input("Enter the number of seconds to count down: "))

# Słowa odpowiadające cyfrom
numbers_in_words = {
    5: "five",
    4: "four",
    3: "three",
    2: "two",
    1: "one"
}

while countdown > 0:
    if countdown <= 5:  # Ostatnie 5 sekund w słowach
        print(numbers_in_words[countdown])
    else:
        print(countdown)
    countdown -= 1
    time.sleep(1)  # Czekaj 1 sekundę

print("Time's up!")