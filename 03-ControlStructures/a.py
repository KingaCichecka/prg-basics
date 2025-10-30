###
# Credit card payment 
#
account_balance = 500
total_payment = int(input("The total price is: "))

if total_payment <= account_balance:
    print('Payment completed')
else:
    print('No funds')