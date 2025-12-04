###
# Sprawdza poprawność nazwy użytkownika i hasła
###

import re

# wczytanie danych z klawiatury
username = input("Enter username: ")
password = input("Enter password: ")

# warunki:
# username: min. 6 znaków, tylko małe litery
username_pattern = r"^[a-z]{6,}$"

# password: min. 8 znaków, litery (małe/duże), cyfry i _
password_pattern = r"^[A-Za-z0-9_]{8,}$"

# sprawdzenie zgodności z wzorcami
username_match = re.match(username_pattern, username)
password_match = re.match(password_pattern, password)

# wydruk wyniku
if username_match and password_match:
    print("Username and password are correct.")
else:
    print("Invalid username and/or password.")
