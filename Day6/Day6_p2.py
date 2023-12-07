with open("./Day6/Day6_Input.txt",'r', encoding="utf-8") as file:
    file_parse = file.read().split('\n')

time = int(''.join(file_parse[0].split(': ')[1].strip(' ').split()))
record = int(''.join(file_parse[1].split(': ')[1].strip(' ').split()))

start = 0

while start * time <= record:
    start += 1
    time -= 1

output = (time + 1 - start)

print(output)
