import re

pattern = re.compile(r"[a-z]+_[a-z]+")
print(pattern.findall("atyrau_chkalov"))