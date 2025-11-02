###
# Buy recommendation if price dropped by at least 10%
#
current_price  = float(input("Current product price: "))
previous_price = float(input("Previous product price: "))

drop_pct = (previous_price - current_price) / previous_price * 100

if drop_pct >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {drop_pct:.0f}%")
else:
    print("Better wait. Drop is less than 10%.")
    print(f"Product price reduced by {drop_pct:.0f}%")
