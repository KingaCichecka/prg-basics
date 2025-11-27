def read_from_file(name):
    with open(name, "r") as file:
        content = file.read()
    return content

file_content = read_from_file("pets.txt")
file_lines = file_content.splitlines()
total_words = 0

for line in file_lines:
    print(line)
    words = line.split()
    total_words += len(words)

print("Total words: ", total_words)
