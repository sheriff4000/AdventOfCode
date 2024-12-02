from helpers import parse_input_into_matrix

matrix = parse_input_into_matrix('inputs/test_input2.txt')

def is_safe(report):
    increasing = all(i < j for i, j in zip(report, report[1:]))
    decreasing = all(i > j for i, j in zip(report, report[1:]))
    if not increasing and not decreasing:
        return False
    if (all(increasing and (1 <= j-i <= 3) for i, j in zip(report, report[1:]))):
        return True
    elif (all(decreasing and (1 <= i-j <= 3) for i, j in zip(report, report[1:]))):
        return True
    return False

def part1():
    total = 0
    
    for report in matrix:
        if is_safe(report):
            total += 1
    
    return total

def part2():
    total = 0
    for report in matrix:
        if is_safe(report):
            total += 1
        else:
            for i in range(len(report)):
                if is_safe(report[:i] + report[i+1:]):
                    total += 1
                    break
            
    return total

print(part2())