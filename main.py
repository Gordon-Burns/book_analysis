import re

from nltk.corpus import stopwords

# Load the book
with open("miracle_in_the_andes.txt", "r", encoding="utf8") as file:
    content = file.read()
    x = re.findall("Chapter [0-9]+", content)

# Print how many chapters in the book
print(x)
print(len(x))

# Which sentences contain the word love

pattern = re.compile("[A-Z]{1}[^.]*[^a-zA-Z]+love[^a-zA-Z]+[^.]*.")
findings = re.findall(pattern, content)
for index, finding in enumerate(findings):
    Num = str(index)
    print(f"{Num} {finding}")
# What are the most used words in the book (Filters out stop words)
pattern = re.compile("[a-zA-Z]+")
words = re.findall(pattern, content.lower())
word_usage = {}
for word in words:
    if word in word_usage.keys():
        word_usage[word] = word_usage[word] + 1
    else:
        word_usage[word] = 1
word_list = [(value, key) for (key, value) in word_usage.items()]
english_stopwords = stopwords.words("english")
filtered_words = []
for count, word in word_list:
    if word not in english_stopwords:
        filtered_words.append((count, word))

sorted_filtered = (sorted(filtered_words,reverse=True))
print(sorted_filtered[0])

# print(sorted(word_list, reverse=True))
