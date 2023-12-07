with open("./Day6/Day6_Input.txt",'r', encoding="utf-8") as file:
    file_parse = file.read().split('\n')

print(file_parse)

time = [int(x) for x in file_parse[0].split(': ')[1].strip(' ').split()]
distance = [int(x) for x in file_parse[1].split(': ')[1].strip(' ').split()]

print(time, distance)

output = 1

for i in range(len(time)):
    curr_time = time[i]
    curr_distance = distance[i]

    start = 0
    end = time[i]

    while start * curr_time <= curr_distance:
        start += 1
        curr_time -= 1

    output *= (curr_time + 1 - start)

print(output)
