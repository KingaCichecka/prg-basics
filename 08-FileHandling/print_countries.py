###
# Reads the entire contents of a file
#
def read_from_file(name):
    with open(name, 'r') as file:
        content = file.read()
    return content

# reads the entire file
file_content = read_from_file('countries.txt')

# splits the entire file contents into lines
file_lines = file_content.splitlines()

# sort alphabetically
file_lines = sorted(file_lines)
# prints the array with numbering
counter = 1
for line in file_lines:
    print(f"{counter}. {line}")
    counter += 1



