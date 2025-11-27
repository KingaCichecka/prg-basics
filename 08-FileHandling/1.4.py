file = open("countries.txt", "r")

for line in file:
    print(line, end="")   # end="" prevents double newlines

file.close()
