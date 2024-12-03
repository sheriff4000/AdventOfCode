import re

instructions = open('inputs/real_input3.txt').read()
print(instructions)


def part1():
    total = 0
    parsed_instructions = re.findall(r'(mul\([0-9]+,[0-9]+\))', instructions)
    for instruction in parsed_instructions:
        total += int(instruction[4:-1].split(',')[0]) * int(instruction[4:-1].split(',')[1])

    return total

def part2():
    total = 0
    active = True
    parsed_instructions = re.findall(r'mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)', instructions)
    for instruction in parsed_instructions:
        if 'do' in instruction:
            active = True
        if 'don\'t' in instruction:
            active = False
        
        if active and 'mul' in instruction:
            total += int(instruction[4:-1].split(',')[0]) * int(instruction[4:-1].split(',')[1])

    return total
print(part2())