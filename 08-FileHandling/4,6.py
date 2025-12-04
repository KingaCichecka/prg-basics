###
# Liczy liczbę samogłosek w podanym tekście
###

import re

text = input("Enter text: ")

# angielskie samogłoski – możesz dodać polskie, np. ąęó…
pattern = r"[aeiouAEIOU]"

vowels = re.findall(pattern, text)
print(f"Number of vowels: {len(vowels)}")
