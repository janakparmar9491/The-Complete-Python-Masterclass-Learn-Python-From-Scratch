import re

pattern = r"eggs"

if re.match(pattern, "eggseggseggs"):
    print("Match found.")
else:
    print("No match found.")