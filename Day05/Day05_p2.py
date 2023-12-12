import copy

with open("./Day05/Day05_Input.txt",'r', encoding="utf-8") as file:
    maps_parse = file.read().split('\n\n')

seed_line_parse = [int(x) for x in maps_parse[0].split(': ')[1].split(' ')]
seed_maps = []
for section in [list(x.split(':\n')[1].split('\n')) for x in maps_parse[1:]]:
    seed_maps.append([])
    for mapped_range in section:
        seed_maps[-1].append([int(x) for x in mapped_range.split(' ')])
    seed_maps[-1] = sorted(seed_maps[-1], key=lambda x:x[1])

print(seed_maps)

# min_seed_location = float('inf')

# for i in range(0, len(seed_line_parse), 2):
#     seed_start, seed_range = seed_line_parse[i], seed_line_parse[i+1]

#     value = 0
#     for seed in range(seed_start, seed_start + seed_range + 1):
#         value = copy.deepcopy(seed)
#         DONE = False
#         for seed_map in seed_maps:
#             for conversion in seed_map:
#                 dest, source, span = conversion
#                 delta = dest - source

#                 if value in range(source, source + span + 1):
#                     value += delta
#                     DONE = True
#                     break

#             if DONE:
#                 DONE = False
#                 continue

#         min_seed_location = min(min_seed_location, value)

#     print("Finished seed range: " + str(i))

# print(min_seed_location)
