###
# Wypisuje plik it_company.csv po 5 linii, między porcjami czeka na Enter
###

FILE_NAME = "it_company.csv"

try:
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        while True:
            # pobierz 5 kolejnych linii
            lines = [next(f, "") for _ in range(5)]
            # jeśli wszystkie puste – koniec pliku
            if not any(lines):
                break

            # wypisz przeczytane linie
            for line in lines:
                if line:
                    print(line.rstrip())

            # jeżeli za chwilę nie ma już następnej linii – nie pytamy o Enter
            pos = f.tell()
            if not f.readline():
                break
            # cofamy o jedną linijkę, bo tylko sprawdzaliśmy czy coś jest
            f.seek(pos)

            input("Press Enter key...")
except FileNotFoundError:
    print(f"File {FILE_NAME} not found.")
