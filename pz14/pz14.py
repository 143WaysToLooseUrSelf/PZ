import re

with open('Dostoevskiy', 'r') as file:
    source_txt = file.read()

reg = r'1857[\s\S]*?(?=^\n\n|\Z)'

match = re.search(reg, source_txt, re.MULTILINE)
if match:
    with open('1857_info.txt', 'w') as new_file:
        new_file.write(match.group(0))
