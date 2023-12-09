def layers(nums, diff):
    if diff == 0:
        return nums[-1]

    new_nums = [(nums[i] - nums[i-1]) for i in range(1, len(nums))]

    # if len(new_nums) == 1:
    #     print('one')
    #     return new_nums[-1]

    return nums[-1] + layers(new_nums, new_nums[0] - new_nums[-1])


# with open("./Day9/Day9_Input.txt",'r', encoding="utf-8") as file:
with open("./Day9/Day9_Input_test.txt",'r', encoding="utf-8") as file:
    file_parse = file.read().split('\n')

output = 0

for line in file_parse:
    nums = [int(num) for num in line.split(' ')]
    output += layers(nums, nums[-1] - nums[-2])

print(output)
