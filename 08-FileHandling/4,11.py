###
# Kopiuje dane książek z wybranego gatunku do osobnego pliku CSV.
###

import csv


def load_books(filename: str) -> list[dict]:
    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def filter_by_genre(books: list[dict], genre: str) -> list[dict]:
    # porównujemy bez uwzględniania wielkości liter
    genre_lower = genre.lower()
    return [b for b in books if b.get("Genre", "").lower() == genre_lower]


def save_books(filename: str, books: list[dict], fieldnames: list[str]) -> None:
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)


def main():
    source_file = "books.csv"
    books = load_books(source_file)

    genre = input("Enter genre to export (e.g. Fiction, Historical): ")

    selected = filter_by_genre(books, genre)

    if not selected:
        print("No books found for this genre.")
        return

    # nazwa pliku na podstawie gatunku
    out_name = genre.lower().replace(" ", "_") + ".csv"

    fieldnames = list(selected[0].keys())
    save_books(out_name, selected, fieldnames)

    print(f"Saved {len(selected)} books of genre '{genre}' to file {out_name}.")


if __name__ == "__main__":
    main()
