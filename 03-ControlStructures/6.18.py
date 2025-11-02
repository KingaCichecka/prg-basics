###
# Yes/No survey with boolean results
#
print("SURVEY")
q1 = input("Are you interested in computer science? (y/n): ").strip().lower() == 'y'
q2 = input("Do you like playing computer games? (y/n): ").strip().lower() == 'y'
q3 = input("Do you have an Instagram account? (y/n): ").strip().lower() == 'y'

print("\nSURVEY RESULTS",
      f"Interested in computer science: {'Yes' if q1 else 'No'}",
      f"Playing computer games: {'Yes' if q2 else 'No'}",
      f"Has an Instagram account: {'Yes' if q3 else 'No'}",
      sep="\n")
