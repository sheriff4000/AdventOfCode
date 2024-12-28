from collections import defaultdict
def match_pattern(pattern, towels, max_towel_len, known_patterns={}):
    if pattern in towels:
        return True
    if pattern in known_patterns:
        return known_patterns[pattern]
    
    for i in range(len(pattern)):
        if pattern[:i+1] in towels and match_pattern(pattern[i+1:], towels, max_towel_len, known_patterns):
            known_patterns[pattern] = True
            return True
        if i >= max_towel_len:
            break
        
    known_patterns[pattern] = False
    return False

def num_ways(pattern, towels, max_towel_len, known_patterns=defaultdict(int)):
    if pattern in known_patterns:
        return known_patterns[pattern]

    for i in range(len(pattern)):
        if pattern[:i+1] in towels:
            known_patterns[pattern] += num_ways(pattern[i+1:], towels, max_towel_len, known_patterns)
        if i >= max_towel_len:
            break
        
    return known_patterns[pattern]
    
    

def part1(patterns, towels):
    known_patterns = {}
    max_towel_len = max(len(towel) for towel in towels)
    return sum(1 for pattern in patterns if match_pattern(pattern, towels, max_towel_len, known_patterns))

def part2(patterns, towels):
    known_patterns = defaultdict(int)
    known_patterns[""] = 1
    max_towel_len = max(len(towel) for towel in towels)
    return sum(num_ways(pattern, towels, max_towel_len, known_patterns) for pattern in patterns)

with open('day19/real.txt') as f:
    towels, patterns = f.read().split("\n\n")
    towels = set(towels.split(", "))
    patterns = patterns.splitlines()

print(part1(patterns, towels))
print(part2(patterns, towels))

# print(match_pattern(pattern, towels))