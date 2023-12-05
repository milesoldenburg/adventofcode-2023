import re

seed_pattern = re.compile(r'seeds: (.*)')
map_pattern = re.compile(r'\n([\d\s]+)+\n', flags=re.MULTILINE)

with open('../input.txt') as f:
    data = f.read()

# Get seeds
m = re.match(seed_pattern, data)
seeds = [int(seed) for seed in m.group(1).strip().split()]

# Get maps
maps = re.findall(map_pattern, data)
maps = [[[int(z) for z in y.split()] for y in x.splitlines()] for x in maps]

locations = []
for seed in seeds:
    for m in maps:
        for r in m:
            dr_start, sr_start, r_length = tuple(r)
            if sr_start <= seed <= sr_start + r_length:
                seed = (seed - sr_start) + dr_start
                break
    locations.append(seed)

print(min(locations))
