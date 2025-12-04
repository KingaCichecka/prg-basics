###
# Oblicza łączną kwotę wydatków z pliku report.txt
###

import re

# nazwa pliku z raportem zakupów
email_file = "report.txt"

# wczytanie treści maila (z polskimi znakami / €)
with open(email_file, "r", encoding="utf-8") as f:
    email = f.read()

# wzorzec wyszukujący kwoty typu 12,34 lub 12.34
pattern = r"\b\d+[.,]\d{2}\b"

# wyciągnięcie wszystkich kwot z tekstu
amounts = re.findall(pattern, email)

# obliczenie sumy
total = 0.0
for amount in amounts:
    # zamiana przecinka na kropkę, żeby dało się rzutować na float
    amount = amount.replace(",", ".")
    total += float(amount)

# wydruk wyniku
print(f"Total money spent: €{total:.2f}")
