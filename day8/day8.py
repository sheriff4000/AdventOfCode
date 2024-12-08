from itertools import combinations
from functools import reduce

def parse_input_into_matrix(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def build_antenna_groups(grid):
    groups = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            val = grid[i][j]
            if val != '.':
                groups[val] = groups.get(val, []) + [(i, j)]

    return groups

def find_antinodes(group, max_x, max_y):
    antinodes = set()
    pairs = combinations(group, 2)
    for pair in pairs:
        first, second = sorted(pair)
        x_diff = second[0] - first[0]
        y_diff = second[1] - first[1]
        antinode_x1 = first[0] + x_diff * 2
        antinode_y1 = first[1] + y_diff * 2

        antinode_x2 = second[0] - x_diff * 2
        antinode_y2 = second[1] - y_diff * 2

        for x, y in [(antinode_x1, antinode_y1), (antinode_x2, antinode_y2)]:
            if 0 <= x < max_x and 0 <= y < max_y:
                antinodes.add((x, y))
    return antinodes

def find_resonant_antinodes(group, max_x, max_y):
    resonant_antinodes = set()
    pairs = combinations(group, 2)
    for pair in pairs:
        first, second = sorted(pair)
        x_diff = second[0] - first[0]
        y_diff = second[1] - first[1]
        resonant_antinode_x = first[0] + x_diff
        resonant_antinode_y = first[1] + y_diff
        while 0 <= resonant_antinode_x < max_x and 0 <= resonant_antinode_y < max_y:
            resonant_antinodes.add((resonant_antinode_x, resonant_antinode_y))
            resonant_antinode_x += x_diff
            resonant_antinode_y += y_diff

        resonant_antinode_x = second[0] - x_diff
        resonant_antinode_y = second[1] - y_diff
        while 0 <= resonant_antinode_x < max_x and 0 <= resonant_antinode_y < max_y:
            resonant_antinodes.add((resonant_antinode_x, resonant_antinode_y))
            resonant_antinode_x -= x_diff
            resonant_antinode_y -= y_diff
    return resonant_antinodes

def part1(filename):
    input_data = parse_input_into_matrix(filename)
    groups = build_antenna_groups(input_data)
    unique_antinodes = reduce(lambda x, y: x.union(y), [find_antinodes(groups[group], len(input_data), len(input_data[0])) for group in groups])
    return len(unique_antinodes)

def part2(filename):
    input_data = parse_input_into_matrix(filename)
    groups = build_antenna_groups(input_data)
    unique_resonant_antinodes = reduce(lambda x, y: x.union(y), [find_resonant_antinodes(groups[group], len(input_data), len(input_data[0])) for group in groups])
    return len(unique_resonant_antinodes)

input_data = parse_input_into_matrix('test.txt')
# print(input_data)

groups = build_antenna_groups(input_data)
# print(build_antenna_groups(input_data))

# print(find_antinodes(groups['A'], len(input_data), len(input_data[0])))

# print(part1('real.txt'))
print(part2('real.txt'))
