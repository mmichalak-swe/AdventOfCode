with open("./Day06/Day06_Input.txt",'r', encoding="utf-8") as file:
    file_parse = file.read().split('\n')

time = int(''.join(file_parse[0].split(': ')[1].strip(' ').split()))
record = int(''.join(file_parse[1].split(': ')[1].strip(' ').split()))

d = (time**2 - (4 * record))**0.5
x1 = (time - (d))/(2)
x2 = (time + (d))/(2)
print(int(x2)-int(x1))
