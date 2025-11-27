###
# Prints employees employed in a specified position (CSV or TXT)
#

file_name = 'it_company.csv'      # lub .txt, zależnie jak masz
job_title = 'Software Engineer'

counter = 1

with open(file_name, 'r') as file:
    for line in file:
        line = line.strip()
        if line == "":
            continue          
       
        if job_title in line:
            print(f"{counter}. {line}")
            counter += 1

