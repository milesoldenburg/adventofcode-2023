import re

part_number_pattern = re.compile(r'(\d+)')
symbol_pattern = re.compile(r'([^.\d\s])')

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

part_num_sum = 0
schematic_line_num = 0
for schematic_line in schematic:
    for part_start, part_end, part_num in schematic_line['parts']:
        left_bound = 0 if part_start == 0 else part_start - 1
        right_bound = line_length if part_end == line_length else part_end + 1

        # Check current line
        for symbol_start, symbol_end, symbol_name in schematic_line['symbols']:
            if left_bound <= symbol_start <= right_bound:
                part_num_sum += int(part_num)

        # Check previous line
        if schematic_line_num > 0:
            for symbol_start, symbol_end, symbol_name in schematic[schematic_line_num - 1]['symbols']:
                if left_bound <= symbol_start <= right_bound:
                    part_num_sum += int(part_num)

        # Check next line
        if schematic_line_num < len(schematic) - 1:
            for symbol_start, symbol_end, symbol_name in schematic[schematic_line_num + 1]['symbols']:
                if left_bound <= symbol_start <= right_bound:
                    part_num_sum += int(part_num)

    schematic_line_num += 1

print(part_num_sum)
