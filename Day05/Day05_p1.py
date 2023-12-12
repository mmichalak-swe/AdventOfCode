import copy

with open("./Day05/Day05_Input.txt",'r', encoding="utf-8") as file:
    file_parse = file.read().split('\n\n')

seed_line_parse = [int(x) for x in file_parse[0].split(': ')[1].split(' ')]
seed_maps = []
for section in [list(x.split(':\n')[1].split('\n')) for x in file_parse[1:]]:
    seed_maps.append([])
    for mapped_range in section:
        seed_maps[-1].append([int(x) for x in mapped_range.split(' ')])

min_seed_location = float('inf')

for seed in seed_line_parse:
    value = copy.deepcopy(seed)
    DONE = False
    for seed_map in seed_maps:
        for conversion in seed_map:
            dest, source, span = conversion
            delta = dest - source

            if value in range(source, source + span + 1):
                value += delta
                DONE = True
                break

        if DONE:
            DONE = False
            continue

    min_seed_location = min(min_seed_location, value)

print(min_seed_location)
