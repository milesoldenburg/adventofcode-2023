import numpy as np
import re

pattern = re.compile(r'([URDL]) (\d+) \(#(.{6})\)')

max_potential_u = 0
max_potential_r = 0
max_potential_d = 0
max_potential_l = 0

plan = []
for line in open('../input.txt'):
    m = re.match(pattern, line)
    direction, distance, color = m.groups()
    distance = int(distance)
    if direction == 'U':
        max_potential_u += distance
    elif direction == 'R':
        max_potential_r += distance
    elif direction == 'D':
        max_potential_d += distance
    elif direction == 'L':
        max_potential_l += distance
    plan.append((direction, distance, color))

max_r = max_potential_r
min_l = max_potential_r
min_u = max_potential_u
max_d = max_potential_u

# Populate grid
data = np.zeros((max_potential_u + max_potential_d + 1, max_potential_l + max_potential_r + 1))
r = max_potential_u
c = max_potential_l
data[r, c] = 1
for direction, distance, color in plan:
    for i in range(distance):
        if direction == 'U':
            r -= 1
        elif direction == 'R':
            c += 1
        elif direction == 'D':
            r += 1
        elif direction == 'L':
            c -= 1
        data[r, c] = 1
        min_l = min(min_l, c)
        max_r = max(max_r, c + 1)
        min_u = min(min_u, r)
        max_d = max(max_d, r + 1)

# Trim grid to actual bounds
data = np.delete(data, np.s_[0:min_u], 0)
data = np.delete(data, np.s_[max_d - min_u:], 0)
data = np.delete(data, np.s_[0:min_l], 1)
data = np.delete(data, np.s_[max_r - min_l:], 1)

for row_i, row in enumerate(data):
    row_string = ''
    for i, e in enumerate(row):
        row_string += str(int(e))
    print(row_string)

print(np.sum(data))
