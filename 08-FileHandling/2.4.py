###
# Saves to a file a list of employees working at a specified position.
#

# file names
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

# Position
job_title = 'Software Engineer'

# write selected employees to a file
with open(position_file, "w") as file:
   with open(employees_file, "r") as source:
      for line in source:
        clean = line.strip()
        if clean == "":
         continue
        if job_title in clean:
            file.write(clean + "\n")

print("Saved in: ", position_file)