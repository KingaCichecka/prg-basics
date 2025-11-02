###
# EAN-13 validator + origin check (590 -> Poland)
#
ean = input("Enter EAN-13 article number: ").strip()

if len(ean) == 13 and ean.isdigit():
    print("Article number is correct")
    if ean.startswith("590"):
        print("Article manufactured in Poland")
else:
    print("Invalid EAN-13 (must be exactly 13 digits)")
