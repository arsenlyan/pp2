import re

text = "Hello My name, is. Arsen"
replacedText = re.sub(r'[ ,.]', ':', text)
print(replacedText)