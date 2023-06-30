import re

from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer as SIA

# Load the book
with open("miracle_in_the_andes.txt", "r", encoding="utf8") as file:
    content = file.read()
    x = re.findall("Chapter [0-9]+", content)
try:
    userinput = int(input("Enter the number for your choice " + "\n"
                          "1. How many chapters in the book " + "\n"
                          "2.Which sentences contain a string " + "\n"
                          "3.Most used words in the book " + "\n"
                          "4.Which chapters are Happy or Sad" + "\n"))
    if userinput == 1:

        # Print how many chapters in the book
        print(len(x))
    elif userinput == 2:
        # Which sentences contain the word love
        search_string = input("What string are you looking for (Enter in Lowercase)")
        pattern = re.compile("[A-Z]{1}[^.]*[^a-zA-Z]+{search_string}[^a-zA-Z]+[^.]*.")
        findings = re.findall(pattern, content)
        for index, finding in enumerate(findings):
            Num = str(index)
            print(f"{Num} {finding}")
    elif userinput == 3:
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

        sorted_filtered = (sorted(filtered_words, reverse=True))
        print(sorted_filtered[0])
    elif userinput == 4:

        # Chapter Analysis
        analyzer = SIA()
        pattern = re.compile("Chapter [0-9]+")
        chapters = re.split(pattern, content)
        for nr, chapter in enumerate(chapters):
            score = analyzer.polarity_scores(chapter)
            print(nr + 1, score)
except ValueError:
    print("Numbers only please")
