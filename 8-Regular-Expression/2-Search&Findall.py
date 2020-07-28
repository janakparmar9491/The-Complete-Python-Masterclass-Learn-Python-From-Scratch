import re

pattern = r"eggs"

if re.match(pattern, "baconeggseggseggs"):
    print("Match found.")
else:
    print("No match found.")

if re.search(pattern, "baconeggseggseggs"):
    print("Match found.")
else:
    print("No match found.")

if re.findall(pattern, "baconeggseggseggs"):
    print("Match found.")
else:
    print("No match found.")

print(re.findall(pattern, "baconeggseggseggs"))
