import re

text = "MyNameIsArsen"

words = re.findall(r'[A-Z][^A-Z]*', text)
print(words)