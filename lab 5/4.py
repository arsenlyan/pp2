import re

pattern = re.compile(r"[A-Z]{1}[a-z]+")
print(pattern.findall("Arsen Lyan programming Principles 2"))