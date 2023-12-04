import re

pattern = re.compile(r'^Card\s+\d+:\s+(.*)\s\|\s+(.*)$')

total_points = 0

for line in open('input.txt'):
    m = re.match(pattern, line)
    winning_numbers = m.group(1).split()
    draws = m.group(2).split()
    matches = 0
    for draw in draws:
        if draw in winning_numbers:
            matches += 1
    if matches > 0:
        total_points += 2 ** (matches - 1)

print(total_points)
