class Region:
    def __init__(self, plant, x, y):
        self.plant = plant
        self.rows = set([x])
        self.cols = set([y])
        self.contained = set([(x, y)])
        self.area = 1
        self.perimeter = 4
        self.sides = 4
        self.max_x = 10
        self.max_y = 10

    def add(self, x, y):
        neighbours = []
        for new_x, new_y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if (new_x, new_y) in self.contained:
                neighbours.append((new_x, new_y))

        surround_count = len(neighbours)
        self.perimeter += 4 - 2 * surround_count

        self.rows.add(x)
        self.cols.add(y)
        self.area += 1
        self.contained.add((x, y))

    def corner_count(self):
        count = 0
        for x, y in self.contained:
            neighbours = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            diagonal_checks = [
                ((neighbours[0], neighbours[2]), (x+1, y+1)),
                ((neighbours[0], neighbours[3]), (x+1, y-1)),
                ((neighbours[1], neighbours[3]), (x-1, y-1)),
                ((neighbours[1], neighbours[2]), (x-1, y+1))
            ]

            for (n1, n2), diag in diagonal_checks:
                if n1 not in self.contained and n2 not in self.contained:
                    count += 1
                elif n1 in self.contained and n2 in self.contained and diag not in self.contained:
                    count += 1
        return count

def plant_regions(data):
    regions = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if not any((i, j) in region.contained for region in regions):
                new_region = Region(data[i][j], i, j)
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    new_points = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
                    for new_x, new_y in new_points:
                        if (0 <= new_x < len(data) and 0 <= new_y < len(data[0]) and 
                            (new_x, new_y) not in new_region.contained and 
                            data[new_x][new_y] == new_region.plant):

                            new_region.add(new_x, new_y)
                            stack.append((new_x, new_y))
                regions.append(new_region)
    return regions

def parse_input_into_matrix(filename):
    with open(filename) as f:
        data = f.read().splitlines()

    return data

data = parse_input_into_matrix("day12/real.txt")

regions = plant_regions(data)
print("part1: ", sum(region.area * region.perimeter for region in regions))
print("part2: ", sum(region.area * region.corner_count() for region in regions))

# print(part1(data))
# print(part2(data))