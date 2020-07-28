import re

pattern = r"^gr.y$"

if re.match(pattern, "grby"):
    print("Match")