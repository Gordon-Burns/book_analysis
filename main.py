import re

# Load the book
with open("miracle_in_the_andes.txt", "r", encoding="utf8") as file:
    content = file.read()
    x = re.findall("Chapter [0-9]+", content)

# Print how many chapters in the book
print(x)
print(len(x))
