from helpers import parse_input_into_two_lists

list1, list2 = parse_input_into_two_lists('real_input1.txt')
def part1():
    total = 0
    list1.sort()
    list2.sort()
    for i in range(len(list1)):
        total += abs(list1[i]-list2[i])

    return total

def part2():
    total = 0
    for item in list1:
        total += item * list2.count(item)

    return total

print(part1())
print(part2())