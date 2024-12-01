
def parse_input_into_two_lists(filename, sort=False):
    with open(filename) as f:
        lines = f.read().splitlines()
    list0 = [line.split() for line in lines]
    list1 = []
    list2 = []
    for line in list0:
        list1.append(int(line[0]))
        list2.append(int(line[1]))
    if sort:
        list1.sort()
        list2.sort()
    return list1, list2