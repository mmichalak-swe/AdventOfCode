import hashlib

with open("./Day04/Day04_Input.txt",'r', encoding="utf-8") as file:
    file_parse = file.read()

input = file_parse
hash = ''
num = 0

while hash[:5] != '00000':
    try_string = input + str(num)
    hash = hashlib.md5(try_string.encode()).hexdigest()
    num += 1

print(num - 1)
