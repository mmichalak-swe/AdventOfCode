import re

with open("./Day05/Day05_Input.txt",'r', encoding="utf-8") as file:
    file_parse = file.read().split('\n')

nice_count = sum(
      1 for s in file_parse
      if len(re.findall(r"([a-z]{2}).*\1", s))
      and re.findall(r"([a-z]).\1", s)
 )

print(nice_count)
