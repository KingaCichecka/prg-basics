###
# Wypisuje imię, nazwisko i email pracowników na stanowisku 'Graphic Designer'
###

import csv

FILE_NAME = "it_company.csv"

print("GRAPHIC DESIGNERS")
print("=================")

with open(FILE_NAME, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # kolumna z nazwą stanowiska może nazywać się np. 'Job Title'
        if row.get("Job Title") == "Graphic Designer":
            first = row.get("First Name", "")
            last = row.get("Last Name", "")
            email = row.get("Email", "")
            print(f"{first} {last},{email}")
