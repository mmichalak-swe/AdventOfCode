with open("./Day06/Day06_Input.txt",'r', encoding="utf-8") as file:
    file_parse = file.read().split('\n')

time = [int(x) for x in file_parse[0].split(': ')[1].strip(' ').split()]
record = [int(x) for x in file_parse[1].split(': ')[1].strip(' ').split()]

output = 1

for i in range(len(time)):
    curr_time = time[i]
    curr_record = record[i]

    start = 0
    end = time[i]

    while start * curr_time <= curr_record:
        start += 1
        curr_time -= 1

    output *= (curr_time + 1 - start)

print(output)
