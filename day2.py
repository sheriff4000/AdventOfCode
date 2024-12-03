from helpers import parse_input_into_matrix

matrix = parse_input_into_matrix('inputs/real_input2.txt')

def is_safe(report):
    pairs = [(report[i], report[i+1]) for i in range(len(report)-1)]
    safe_increasing = all((1 <= j-i <= 3) for i, j in pairs)
    safe_decreasing = all((1 <= i-j <= 3) for i, j in pairs)
    
    return safe_increasing or safe_decreasing

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

print(part1())
print(part2())
