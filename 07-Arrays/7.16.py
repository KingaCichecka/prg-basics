# Sort from lowest to highest
distances_traveled = [120, 150, 180, 90, 200, 175, 160]
distances_traveled_sorted = sorted(distances_traveled)
print(distances_traveled_sorted)

# Sort in descending order, highest to lowest
daily_temperatures = [16, 17, 15, 14, 18, 19, 17, 15, 16, 18]
daily_temperatures_sorted = sorted(daily_temperatures, reverse=True)
print(daily_temperatures_sorted)

# Sort file names in ascending alphabetical order
file_names = ["report.docx", "presentation.pptx", "data.csv", "photo.jpg", "notes.txt",
              "invoice.pdf", "resume.docx", "budget.xlsx", "meeting.mp4", "schedule.pdf"]
file_names_sorted = sorted(file_names)
print(file_names_sorted)
