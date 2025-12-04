###
# Wypisuje produkty z clothing.csv, których cena < 60 i stan magazynowy < 40
###

import csv

FILE_NAME = "clothing.csv"

with open(FILE_NAME, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # przykładowe nazwy kolumn – dostosuj jeśli w pliku są inne
        price = float(row.get("Price", "0"))
        stock = int(row.get("Stock", "0"))

        if price < 60 and stock < 40:
            print(f"{row.get('Product', '')} – price: {price}, stock: {stock}")
