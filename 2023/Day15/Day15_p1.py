with open("./Day15/Day15_Input.txt",'r', encoding="utf-8") as file:
    file_parse = file.read().split(',')

output = 0
for seq in file_parse:
    temp = 0
    for char in seq:
        temp += ord(char)
        temp *= 17
        temp = temp % 256
    output += temp

print(output)
