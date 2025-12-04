###
# Liczy linie, znaki i słowa w podanym pliku tekstowym
###

import re

file_name = input("Enter file name: ")

try:
    with open(file_name, "r", encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError:
    print(f"File {file_name} does not exist.")
else:
    lines = content.splitlines()
    num_lines = len(lines)
    num_chars = len(content)
    # jako słowa liczymy sekwencje znaków alfanumerycznych
    num_words = len(re.findall(r"\b\w+\b", content))

    print(f"File name: {file_name}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of characters: {num_chars}")
    print(f"Number of words: {num_words}")
