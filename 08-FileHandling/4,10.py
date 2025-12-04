###
# Oblicza, wypisuje i zapisuje do pliku potęgi 1..100
###

OUTPUT_FILE = "powers.txt"

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for n in range(1, 101):
        n2 = n ** 2
        n3 = n ** 3
        line = f"{n},{n2},{n3}"
        print(line)
        f.write(line + "\n")

print(f"Results saved in {OUTPUT_FILE}")
