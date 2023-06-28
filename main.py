import re

# Load the book
with open("miracle_in_the_andes.txt", "r", encoding="utf8") as file:
    content = file.read()
    x = re.findall("Chapter [0-9]+", content)

# Print how many chapters in the book
print(x)
print(len(x))

# Which sentences contain the word love

pattern = re.compile("[A-Z]{1}[^.]*[^a-zA-Z]+love[^a-zA-Z]+[^.]*.")
findings = re.findall(pattern,content)
for index,finding in enumerate(findings):
    Num = str(index)
    print(f"{Num} {finding}")
