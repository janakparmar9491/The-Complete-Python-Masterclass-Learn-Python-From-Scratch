import re

pattern = r"[A-Z][A-Z][0-9]"

if re.search(pattern, "AA1"):
    print("Match found.")