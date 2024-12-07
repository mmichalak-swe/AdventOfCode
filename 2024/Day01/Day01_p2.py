output = 0
list_one = []
dict_two = {}


with open('./Day01/Day01_Input.txt','r', encoding="utf-8") as myfile:
    for line in myfile:
        first, second = line.strip().split("  ")
        first, second = int(first), int(second)

        list_one.append(first)
        dict_two[second] = dict_two.get(second, 0) + 1

    for num in list_one:
        output += num * dict_two.get(num, 0)

print(output)
