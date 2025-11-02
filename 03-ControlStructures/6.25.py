
CORRECT_PIN = "0805"
attempts = 0

while attempts < 3:
    pin = input("Enter the PIN code: ")
    if pin == CORRECT_PIN:
        print("Correct. Welcome!")
        break
    else:
        print("Incorrect...")
        attempts += 1
else:
    print("Sorry, your payment card has been blocked.")
