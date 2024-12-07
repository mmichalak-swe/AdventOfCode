output = 0
list_one = []
list_two = []


with open('./Day01/Day01_Input.txt','r', encoding="utf-8") as myfile:
    for line in myfile:
        first, second = line.strip().split("  ")
        first, second = int(first), int(second)

        list_one.append(first)
        list_two.append(second)

    list_one.sort()
    list_two.sort()

    for i in range(len(list_one)):
        output += abs(list_one[i] - list_two[i])

print(output)
