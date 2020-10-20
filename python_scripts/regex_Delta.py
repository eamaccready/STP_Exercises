import re

# Read in file.
with open ("zen.txt", "r") as file:
    text = file.read()

word = re.findall("Dutch", text)

print(word)
