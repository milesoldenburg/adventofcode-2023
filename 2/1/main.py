import re

pattern = re.compile(r'^Game (\d+): (.*)$')
possible_game_id_sum = 0

for line in open('input.txt'):
    match = re.match(pattern, line)
    if match:
        game_id = match.group(1)
        draws = match.group(2)
        is_game_possible = True
        for draw in draws.split(';'):
            for types in draw.strip().split(','):
                count, color = types.strip().split(' ', 1)
                if any([
                    color == 'red' and int(count) > 12,
                    color == 'green' and int(count) > 13,
                    color == 'blue' and int(count) > 14,
                ]):
                    is_game_possible = False
                    break
            if not is_game_possible:
                break
        if is_game_possible:
            possible_game_id_sum += int(game_id)

print(possible_game_id_sum)
