import re

seed_pattern = re.compile(r'seeds: (.*)')
seed_pair_pattern = re.compile(r'(\d+ \d+)')
map_pattern = re.compile(r'\n([\d\s]+)+\n', flags=re.MULTILINE)

with open('../input.txt') as f:
    data = f.read()

# Get seeds
m = re.match(seed_pattern, data)
seed_pairs = [[int(y) for y in x.split()] for x in re.findall(seed_pair_pattern, m.group(1))]
seed_pairs.sort(key=lambda x: x[0])

# Get maps
maps = re.findall(map_pattern, data)
maps = [[[int(z) for z in y.split()] for y in x.splitlines()] for x in maps]
maps.reverse()

for i in range(1, 4269624552):
    location = i
    for m in maps:
        for r in m:
            dr_start, sr_start, r_length = tuple(r)
            if dr_start <= i <= dr_start + r_length:
                i = (i - dr_start) + sr_start
                break
    for seed_pair in seed_pairs:
        if seed_pair[0] <= i <= seed_pair[0] + seed_pair[1]:
            print(location)
            exit()
