import re

time_pattern = re.compile(r'Time:\s+(.*)')
distance_pattern = re.compile(r'Distance:\s+(.*)')

with open('../input.txt') as f:
    data = f.read()

times = re.search(time_pattern, data)
distances = re.search(distance_pattern, data)

t = int(re.sub(r'\s', '', times.group(1)))
d = int(re.sub(r'\s', '', distances.group(1)))

total_wins = []
wins = 0
for i in range(1, t):
    travels = i * (t - i)
    if travels > d:
        wins += 1

print(wins)
