###
# Wypisuje nazwy plików, których rozszerzenie ma dokładnie 4 znaki
###

FILE_NAME = "files.txt"

with open(FILE_NAME, "r", encoding="utf-8") as f:
    for line in f:
        name = line.strip()
        if not name:
            continue
        if "." not in name:
            continue

        base, ext = name.rsplit(".", 1)
        if len(ext) == 4:   # dokładnie 4 znaki
            print(name)
