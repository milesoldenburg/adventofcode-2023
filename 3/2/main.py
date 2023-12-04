import re

part_number_pattern = re.compile(r'(\d+)')
symbol_pattern = re.compile(r'(\*)')

line_number = 0
line_length = 0
schematic = []
for line in open('input.txt'):
    if line_number == 0:
        line_length = len(line.strip())

    schematic_line = {
        'parts': [],
        'symbols': []
    }

    for m in re.finditer(part_number_pattern, line):
        schematic_line['parts'].append((m.start(), m.end() - 1, m.group(0)))

    for m in re.finditer(symbol_pattern, line):
        schematic_line['symbols'].append((m.start(), m.end() - 1, m.group(0)))

    schematic.append(schematic_line)
    line_number += 1

gear_ratio_sum = 0
schematic_line_num = 0
for schematic_line in schematic:
    for symbol_start, symbol_end, symbol_name in schematic_line['symbols']:
        adjacent_parts = []
        left_bound = 0 if symbol_start == 0 else symbol_start - 1
        right_bound = line_length if symbol_end == line_length else symbol_end + 1

        # Check current line
        for part_start, part_end, part_name in schematic_line['parts']:
            if part_start <= left_bound <= part_end or part_start <= symbol_start <= part_end or part_start <= right_bound <= part_end:
                adjacent_parts.append(int(part_name))

        # Check previous line
        if schematic_line_num > 0:
            for part_start, part_end, part_name in schematic[schematic_line_num - 1]['parts']:
                if part_start <= left_bound <= part_end or part_start <= symbol_start <= part_end or part_start <= right_bound <= part_end:
                    adjacent_parts.append(int(part_name))

        # Check next line
        if schematic_line_num < len(schematic) - 1:
            for part_start, part_end, part_name in schematic[schematic_line_num + 1]['parts']:
                if part_start <= left_bound <= part_end or part_start <= symbol_start <= part_end or part_start <= right_bound <= part_end:
                    adjacent_parts.append(int(part_name))

        if len(adjacent_parts) == 2:
            gear_ratio = adjacent_parts[0] * adjacent_parts[1]
            gear_ratio_sum += gear_ratio

    schematic_line_num += 1

print(gear_ratio_sum)
