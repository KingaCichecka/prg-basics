text = "An apple a day keeps the doctor away"

# Module MyText – funkcje operujące na tekście

def word_count(txt):
    words = txt.split()
    return len(words)

def words_longest_first(txt):
    words = txt.split()
    # sortowanie po długości malejąco
    for i in range(len(words)):
        for j in range(0, len(words) - i - 1):
            if len(words[j]) < len(words[j + 1]):
                words[j], words[j + 1] = words[j + 1], words[j]
    return words

def words_alphabetical(txt):
    words = txt.split()
    # zwykłe sortowanie alfabetyczne (bez built-in)
    for i in range(len(words)):
        for j in range(0, len(words) - i - 1):
            if words[j].lower() > words[j + 1].lower():
                words[j], words[j + 1] = words[j + 1], words[j]
    return words

# Program korzystający z MyText
print("Text:", text)
print("Number of words:", word_count(text))
print("Words from the longest:", ",".join(words_longest_first(text)))
print("Words ordered alphabetically:", ",".join(words_alphabetical(text)))
