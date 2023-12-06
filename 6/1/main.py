import math
import re

time_pattern = re.compile(r'Time:\s+(.*)')
distance_pattern = re.compile(r'Distance:\s+(.*)')

with open('../input.txt') as f:
    data = f.read()

times = re.search(time_pattern, data)
distances = re.search(distance_pattern, data)

times = [int(t) for t in times.group(1).split()]
distances = [int(d) for d in distances.group(1).split()]

total_wins = []
for ti, t in enumerate(times):
    d = distances[ti]
    wins = 0
    for i in range(1, t):
        travels = i * (t - i)
        if travels > d:
            wins += 1
    if wins > 0:
        total_wins.append(wins)

print(math.prod(total_wins))
