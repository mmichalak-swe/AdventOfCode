def check(nums):
    return all(x == nums[0] for x in nums)


def layers(nums):
    if check(nums) is True:
        return nums[-1]
    new_nums = [(nums[i] - nums[i-1]) for i in range(1, len(nums))]
    return nums[-1] + layers(new_nums)


with open("./Day09/Day09_Input.txt",'r', encoding="utf-8") as file:
    file_parse = file.read().split('\n')

output = 0

for line in file_parse:
    nums = [int(num) for num in line.split(' ')]
    output += layers(nums)

print(output)
