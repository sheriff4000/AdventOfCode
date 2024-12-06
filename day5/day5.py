
with open('real_input5.txt') as f:
    lines = f.read()

rules, pages = lines.split('\n\n')

def parse_rules(ruleset):
    rules = ruleset.split('\n')
    rules = [(rule[:rule.find('|')], rule[rule.find('|')+1:]) for rule in rules]
    rule_dict = {}
    for rule in rules:
        if rule[0] in rule_dict:
            rule_dict[rule[0]].add(rule[1])
        else:
            rule_dict[rule[0]] = set([rule[1]])
    return rule_dict

def is_valid(update):
    for idx in range(len(update)):
        before_list = update[:idx]
        for page in before_list:
            if page in ruleset.get(update[idx], {}):
                return False
    return True

def sort_pages(in_pages):
    out = in_pages.copy()
    for i, page in enumerate(in_pages):
        idx = i
        earliest_index = idx
        for rule in ruleset.get(page, {}):
            if rule in in_pages:
                earliest_index = min(earliest_index, out.index(rule) if rule in in_pages else len(in_pages)-1)
        
        if earliest_index != idx:
            out.insert(earliest_index, out.pop(idx))
    return out

def part1():
    total = 0
    for update in pages.splitlines():
        update = update.split(',')
        if is_valid(update):
            mid = len(update) // 2
            total += int(update[mid])
    return total

def part2():
    total = 0
    for update in pages.splitlines():
        update = update.split(',')
        if not is_valid(update):
            sorted_update = sort_pages(update)
            mid = len(sorted_update) // 2
            total += int(sorted_update[mid])
    return total
ruleset = parse_rules(rules)

print(part1())
print(part2())

# print(part2())