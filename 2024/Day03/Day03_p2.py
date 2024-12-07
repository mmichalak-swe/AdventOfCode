import re

with open('./Day03/Day03_Input.txt','r', encoding="utf-8") as myfile:
    corrupted_memory = myfile.read()

    corrupted_memory = re.sub(r"don't\(\).*?(?=do\(\)|$)", "", corrupted_memory, flags=re.DOTALL)
    occurences = re.findall("mul\(\d+,\d+\)", corrupted_memory)
    digits = [re.findall("\d+", occurence) for occurence in occurences]

print(sum([int(pair[0]) * int(pair[1]) for pair in digits]))
