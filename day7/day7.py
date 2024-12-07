from itertools import product
from functools import reduce

with open('real.txt') as f:
    lines = f.read().splitlines()

def split_target(line):
    target, rest = line.split(': ')
    rest = rest.split(' ')
    return int(target), [int(x) for x in rest]

def reducer(x, y):
    if y[0] == '+':
        return x + y[1]
    elif y[0] == '*':
        return x * y[1]
    else:
        return int(str(x) + str(y[1]))

def check_valid(target, rest, operators):
    num_operators = len(rest) - 1
    if num_operators == 0 and rest[0] != target:
        return False
    perms = product(operators, repeat=num_operators)
    for perm in perms:
        ops_val = zip(perm, rest[1:])
        out = reduce(reducer, ops_val, rest[0])
        if out == target:
            return True
            
    return False

def solve(lines, operators):
    res = 0
    for line in lines:
        target, rest = split_target(line)
        if check_valid(target, rest, operators):
            res += target
    return res

def part1(lines):
    return solve(lines, ['+', '*'])

def part2(lines):
    return solve(lines, ['+', '*', '||'])

print("part 1: ", part1(lines))
print("part 2: ", part2(lines))