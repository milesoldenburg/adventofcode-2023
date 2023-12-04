import re

pattern = re.compile(r'^Game (\d+): (.*)$')
power_set_sum = 0

for line in open('input.txt'):
    match = re.match(pattern, line)
    if match:
        game_id = match.group(1)
        draws = match.group(2)
        max_red = 0
        max_green = 0
        max_blue = 0
        for draw in draws.split(';'):
            for types in draw.strip().split(','):
                count, color = types.strip().split(' ', 1)
                if color == 'red' and int(count) > max_red:
                    max_red = int(count)
                if color == 'green' and int(count) > max_green:
                    max_green = int(count)
                if color == 'blue' and int(count) > max_blue:
                    max_blue = int(count)
        power_set = max_red * max_green * max_blue
        power_set_sum += power_set

print(power_set_sum)
