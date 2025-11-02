###
# ATM (cash machine) simulator with PIN verification and PIN change
#
balance = 1000  # Initial balance
pin = '1111'    # Initial 4-digit PIN code

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("5. Check PIN")
    print("6. Change PIN")

    choice = input("Choose an option (1–6): ")
    print()

    # --- CHECK BALANCE ---
    if choice == '1':
        entered_pin = input("Enter your PIN: ")
        if entered_pin == pin:
            print(f"Your current balance is: €{balance}")
        else:
            print("Incorrect PIN.")

    # --- DEPOSIT ---
    elif choice == '2':
        entered_pin = input("Enter your PIN: ")
        if entered_pin == pin:
            amount = float(input("Enter the amount to deposit: "))
            balance += amount
            print(f"€{amount} has been deposited. New balance: €{balance}")
        else:
            print("Incorrect PIN.")

    # --- WITHDRAW ---
    elif choice == '3':
        entered_pin = input("Enter your PIN: ")
        if entered_pin == pin:
            amount = float(input("Enter the amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"€{amount} has been withdrawn. New balance: €{balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Incorrect PIN.")

    # --- EXIT ---
    elif choice == '4':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop

    # --- CHECK PIN ---
    elif choice == '5':
        entered_pin = input("Enter your PIN: ")
        if entered_pin == pin:
            print("PIN is correct.")
        else:
            print("Incorrect PIN.")

    # --- CHANGE PIN ---
    elif choice == '6':
        old_pin = input("Enter your current PIN: ")
        if old_pin == pin:
            new_pin = input("Enter your new 4-digit PIN: ")
            if new_pin.isdigit() and len(new_pin) == 4:
                pin = new_pin
                print("PIN successfully changed!")
            else:
                print("Invalid PIN. It must contain exactly 4 digits.")
        else:
            print("Incorrect current PIN.")

    # --- INVALID OPTION ---
    else:
        print("Invalid option. Please try again.")
